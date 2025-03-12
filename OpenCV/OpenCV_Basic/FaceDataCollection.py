import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
name = input("Enter the Name of the Person: ")
face_data = []
count = 0
while True:
    ret,frame = cap.read()
    
    if ret == False:
        continue

    faces = face_classifier.detectMultiScale(frame,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),[255,0,0],2)
    cv2.imshow('Captured Image',frame)

    if len(faces) == 0:
        continue
        
    face = sorted(faces,key = lambda f:f[2]*f[3])[-1]
    x,y,w,h = face
    offset = 10
    face_img = frame[y-offset:y+h+offset, x-offset:x+w+offset]
    face_img = cv2.resize(face_img,(100,100))
    cv2.imshow('Face Image',face_img)
    count += 1

    if count%10 == 0:
        face_data.append(face_img.flatten())
        print(len(face_data))
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

face_data = np.array(face_data)
print(face_data.shape)

np.save('./data/'+name+'.npy',face_data)

cap.release()
cv2.destroyAllWindows()