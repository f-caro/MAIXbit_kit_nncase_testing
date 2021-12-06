import utime, lcd
from Maix import GPIO

lcd.init()

slow = 0
def test_irq(GPIO ):
    global slow    
    slow += 1
    print("key: ", slow )
    strTemp = str(slow)
    lcd.draw_string(10,10, strTemp , lcd.WHITE, lcd.BLACK)
   
def inc_slow_counter(GPIO):    
    global slowCounter, fastCounter    
    slowCounter += 1
    fastCounter = 0
    print("slow count: ", slowCounter, "\n")
    strTemp = "Slow Counter: " + slowCounter
    lcd.draw_string(10,10, strTemp , lcd.WHITE, lcd.BLACK)

#fm.register(board_info.BOOT_KEY,fm.fpioa.GPIOHS0)
fm.register(GPIO.GPIOHS9,fm.fpioa.GPIOHS9)

key=GPIO(GPIO.GPIOHS9,GPIO.IN,GPIO.PULL_DOWN)
utime.sleep_ms(500)
key.value()
key.irq(test_irq,GPIO.IRQ_RISING,GPIO.WAKEUP_NOT_SUPPORT,7)

#key.disirq()
#fm.unregister(board_info.BOOT_KEY,fm.fpioa.GPIOHS0)
