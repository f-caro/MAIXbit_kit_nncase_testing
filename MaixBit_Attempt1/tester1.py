import lcd
import os
import utime

from Maix import GPIO

def inc_slow_counter(GPIO, pin_num):    
    slowCounter += 1
    fastCounter = 0
    print("pin_num", pin_num)
    print("slow count: ", slowCounter, "\n")
    strTemp = "Slow Counter: " + str(slowCounter)
    lcd.draw_string(10,10, strTemp , lcd.WHITE, lcd.BLACK)
    strTemp = "Fast Counter: " + str(fastCounter)
    lcd.draw_string(10,100, strTemp, lcd.WHITE, lcd.BLACK)

def inc_fast_counter(GPIO,pin_num):
    fastCounter += 1
    print("fast count: ", fastCounter , "\n")
    strTemp = "Fast Counter: " + fastCounter
    lcd.draw_string(10,100, strTemp, lcd.WHITE, lcd.BLACK)

lcd.init()

slowCounter = 0
pinSlowCount = GPIO(GPIO.GPIOHS9, GPIO.IN, GPIO.PULL_DOWN )
pinSlowCount.pull(GPIO.IRQ_RISING)
pinSlowCount.value(0)
pinSlowCount.irq(inc_slow_counter, GPIO.IRQ_RISING, GPIO.WAKEUP_NOT_SUPPORT, 7 )


#pinFastCount = GPIO(GPIO.GPIOHS10, GPIO.IN, GPIO.PULL_DOWN)
fastCounter = 0

#pinFastCount.irq(inc_fast_counter, GPIO.IRQ_RISING, GPIO.WAKEUP_NOT_SUPPORT, 7 )

lcd.draw_string(200,100, "Starting up", lcd.WHITE, lcd.BLACK)

while(True):
   slow=0
    


pinSlowCount.disirq()
#pinFastCount.disirq()

