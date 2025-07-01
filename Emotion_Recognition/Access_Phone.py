from facial_emotion_recognition import EmotionRecognition
import urllib.request
import cv2
import numpy as np
import imutils


er = EmotionRecognition(device='cpu')           #Algorihm
url = 'http://10.248.65.79:8080/shot.jpg'       #URL for accessing cemara

while True:
    impath = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(impath.read()),dtype=np.uint8)       #Converting number into array

    frame = cv2.imdecode(imgnp,-1)                 #Decoding the Numberes into img
    frame = er.recognise_emotion(frame,return_type="BGR")
    frame = imutils.resize(frame,width=450)

    cv2.imshow("frame",frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.release()
