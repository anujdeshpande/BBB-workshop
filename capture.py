import cv

camcapture = cv.CreateCameraCapture(0)
cv.SetCaptureProperty(camcapture,cv.CV_CAP_PROP_FRAME_WIDTH, 480)
cv.SetCaptureProperty(camcapture,cv.CV_CAP_PROP_FRAME_HEIGHT, 640);

if not camcapture:
        print "Error opening WebCAM"
        sys.exit(1)

frame = cv.QueryFrame(camcapture)
cv.SaveImage('out.png',frame)
