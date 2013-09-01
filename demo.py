import tornado.ioloop
import tornado.web
import time
import Adafruit_BBIO.GPIO as GPIO
import cv

GPIO.setup("P8_10", GPIO.OUT)
i=1
intruder=0
while(True):
    # run this loop till there is a change in the image
    i=i+1
    if(i=10):
        break
intruder=1

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
