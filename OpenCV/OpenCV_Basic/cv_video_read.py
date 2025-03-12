import cv2

cap = cv2.VideoCapture(0)
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

while True:
    ret,frame = cap.read()
    
    if ret == False:
        continue

    faces = face_classifier.detectMultiScale(frame,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),[255,0,0],2)
        
    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Captured Image',frame)
    # cv2.imshow('GrayScale',gray)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()