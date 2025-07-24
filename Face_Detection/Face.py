import cv2
alg = "haarcascade_frontalface_default.xml"
haar_cascade= cv2.CascadeClassifier(alg)

com = cv2.VideoCapture(0) #id for camera

while True:
    _,img = com.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(gray,(1.3),4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),5)

    cv2.imshow("FaceDect",img)

    key = cv2.waitKey(5)
    #print(key)
    if key == ord("q"):
        break
    
com.release()
cv2.destrouAllWindow()
