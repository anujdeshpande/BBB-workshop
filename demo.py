import tornado.ioloop
import tornado.web
import time
import Adafruit_BBIO.GPIO as GPIO
import cv,cv2

GPIO.setup("P8_10", GPIO.OUT)
intruder = 1

def blink():
    for i in range(0, 5):
        GPIO.output("P8_10", GPIO.HIGH)
        time.sleep(1)
        GPIO.output("P8_10",GPIO.LOW);
        time.sleep(1)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if(intruder):
            self.write("Intruder Alert")
            blink()
        else:
            self.write("Safe and secure")
        
application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
