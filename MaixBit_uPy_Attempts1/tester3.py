import utime, lcd
from Maix import GPIO


lcd.init()
lcd.direction(lcd.YX_LRUD)

slowCounter = 0
fastCounter = 0
time_t0 = utime.ticks_ms()

def report_slow_counters_to_lcd(slowCounter, fastCounter):
    lcd.draw_string(10,10, "Slow Counter: " , lcd.WHITE, lcd.BLACK)
    lcd.draw_string(120,10, "     " , lcd.WHITE, lcd.BLACK)
    lcd.draw_string(120,10, str(slowCounter) , lcd.WHITE, lcd.BLACK)
    return

def report_fast_counters_to_lcd(slowCounter, fastCounter):
    lcd.draw_string(10,100, "Fast Counter: ", lcd.WHITE, lcd.BLACK)
    lcd.draw_string(120,100, "     ", lcd.WHITE, lcd.BLACK)
    lcd.draw_string(120,100, str(fastCounter), lcd.WHITE, lcd.BLACK)
    return
  
#def report_counter_timing(time_diff_ms):
#    global time_t0
#    lcd.draw_string(250,10, str( time_diff_ms ), lcd.WHITE, lcd.BLACK)

def inc_slow_counter(GPIO):    
    global slowCounter, fastCounter, time_t0, uart1
    slowCounter += 1
    time_diff_ms = utime.ticks_diff(utime.ticks_ms(), time_t0)    
    time_t0 = utime.ticks_ms()  #update time_t0 with new time
    uartStr = "Grueso#" + str(slowCounter) + " : Fino#" + str(fastCounter)
    uartStr += " - " + str(time_diff_ms) + " ms "  + "\n"
    print(uartStr)
    eg1 = bytearray()
    eg1.append(0x30)
    test22= str('6', 'UTF-8')
    uart1.write( bytearray('6' , 'ASCII') )
    #uart1.write( bytearray(uartStr) )    
    report_slow_counters_to_lcd(slowCounter, fastCounter)
    fastCounter = 0
    report_fast_counters_to_lcd(slowCounter, fastCounter)
    

def inc_fast_counter(GPIO):    
    global slowCounter, fastCounter    
    fastCounter += 1
    #print("fast count: ", fastCounter, "\n")
    report_fast_counters_to_lcd(slowCounter, fastCounter)

#Map fpioa hardware definition of PIN to class GPIO software definition of PIN
fm.register(GPIO.GPIOHS9,fm.fpioa.GPIOHS9)
fm.register(GPIO.GPIOHS10,fm.fpioa.GPIOHS10)

fm.register(GPIO.GPIOHS7,fm.fpioa.UART1_TX)
fm.register(GPIO.GPIOHS8,fm.fpioa.UART1_RX)

#uart1 = machine.UART(machine.UART.UART1,
#                    baudrate=9600,bits=8,parity=None,stop=1,
#                    timeout=1000, buf_size=1024, lineend=b'\r\n' , read_buf_len=4096 )

uart1 = machine.UART(machine.UART.UART1,
                    baudrate=4800,bits=8,parity=None,stop=1,
                    timeout=1000, read_buf_len=4096 )


#uart1 = machine.UART(machine.UART.UART1, 4800)
#uart1.init(baudrate=4800,bits=8,parity=None,stop=1,
#                    timeout=1000 )# , read_buf_len=4096 )


#Instantiate GPIO and define properties of PINs
slowCountPin=GPIO(GPIO.GPIOHS9,GPIO.IN,GPIO.PULL_DOWN)
fastCountPin=GPIO(GPIO.GPIOHS10,GPIO.IN,GPIO.PULL_DOWN)

#leave a tiny delay ... why, I don't know... so for magic reasons...
utime.sleep_ms(500)


#read pin values into memory, then define Interrupt function requests
slowCountPin.value()
slowCountPin.irq(inc_slow_counter,GPIO.IRQ_RISING,GPIO.WAKEUP_NOT_SUPPORT,7)

fastCountPin.value()
fastCountPin.irq(inc_fast_counter,GPIO.IRQ_RISING,GPIO.WAKEUP_NOT_SUPPORT,7)

report_slow_counters_to_lcd(0, 0)
report_fast_counters_to_lcd(0, 0)
#key.disirq()
#fm.unregister(board_info.BOOT_KEY,fm.fpioa.GPIOHS0)

while (True):
    uart1.write(bytearray( b'A', 'ASCII') )
