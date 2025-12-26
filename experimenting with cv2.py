import cv2
vid=cv2.VideoCapture(0)
while vid.isOpened():
    ret,frame=vid.read()
    if not ret:
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blured=cv2.GaussianBlur(gray,(7,7),0)
    can=cv2.Canny(blured,50,150)
    copy=frame.copy()
    cont,hier=cv2.findContours(can,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in cont:
        if cv2.contourArea(cnt)>100:
            x,y,w,h=cv2.boundingRect(cnt)
            cv2.rectangle(copy,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('frame',copy)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()