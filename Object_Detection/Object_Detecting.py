import cv2
import imutils
com = cv2.VideoCapture(0)

fframe = None
area = 500

while True:

    _,img = com.read()
    text="Normal"

    img = imutils.resize(img,width=1000)
    gimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gausimg = cv2.GaussianBlur(gimg,(21,21),0)

    if fframe is None:
        fframe = gausimg
        continue
    
    imgdif = cv2.absdiff(fframe,gausimg)
    threshimg = cv2.threshold(imgdif,25,255,cv2.THRESH_BINARY)[1]
    #threshimg = cv2.dilate(threshimg,None, iteration=2)

    cnts = cv2.findContours(threshimg.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        if cv2.contourArea(c) < area:
            continue
        (x,y,w,h) = cv2.boundingRect(c)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

        text = "Moving Object Detected"
    #print(text)

    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)

    cv2.imshow("Object is Moving",img)

    key = cv2.waitKey(10)
    #print(key)
    if key == ord('q'):
        break

com.relese()
cv2.destroyAllWindow()








        
