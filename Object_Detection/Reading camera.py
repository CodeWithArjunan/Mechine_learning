import cv2

com = cv2.VideoCapture(0)

while True:
    _,img = com.read()
    cv2.imshow("show",img)
    key = cv2.waitKey(1)
    if key == ord("a"):
        break
com.release()
cv2.destroyAllWindow()
