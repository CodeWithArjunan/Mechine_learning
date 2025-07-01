from facial_emotion_recognition import EmotionRecognition       
import cv2

er = EmotionRecognition(device='cpu')    #Algorithm for Emotion finding

cam = cv2.VideoCapture(0) #id

while True:
    _,img = cam.read() #read
    img = er.recognise_emotion(img,return_type='BGR')

    cv2.imshow("Frame",img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindow()
