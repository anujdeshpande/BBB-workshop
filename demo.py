import time
import Adafruit_BBIO.GPIO as GPIO
import cv,cv2

GPIO.setup("P8_10", GPIO.OUT)

from flask import Flask
app = Flask(__name__)

def blink():
    for i in range(0, 5):
        GPIO.output("P8_10", GPIO.HIGH)
        time.sleep(1)
        GPIO.output("P8_10",GPIO.LOW);
        time.sleep(1)

@app.route("/")

def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
    GPIO.cleanup()
