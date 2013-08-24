import time
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P8_10", GPIO.OUT)
for i in range(0, 10):
    GPIO.output("P8_10", GPIO.HIGH)
    time.sleep(1)
    GPIO.output("P8_10",GPIO.LOW);
    time.sleep(1)

GPIO.cleanup()
