#programa para hacer video continuo con threading
from imutils.video.pivideostream import * # funciona mejor asi
from imutils.video import FPS
import argparse
import imutils
import time
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=80,
    help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=-1,
    help="Whether or not frames should be displayed")
args = vars(ap.parse_args())
vs = PiVideoStream().start()
time.sleep(2.0) # espera que caliente la camara
#fps = FPS().start()
while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=640)
    if args["display"] > 0:
        frame= cv2.flip(frame,0)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    #fps.update()
    #fps.stop()
cv2.destroyAllWindows()
vs.stop()
