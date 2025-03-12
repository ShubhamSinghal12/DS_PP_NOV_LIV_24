# Recognise Faces using some classification algorithm - like Logistic, KNN, SVM etc.


# 1. load the training data (numpy arrays of all the persons)
		# x- values are stored in the numpy arrays
		# y-values we need to assign for each person
# 2. Read a video stream using opencv
# 3. extract faces out of it
# 4. use knn to find the prediction of face (int)
# 5. map the predicted id to name of the user 
# 6. Display the predictions on the screen - bounding box and name

import os
import numpy as np
import cv2
from sklearn.neighbors import KNeighborsClassifier

cap = cv2.VideoCapture(0)
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
face_data = []
face_labels = []
name = {}
cid = 0
for file in os.listdir('./data'):
    if file.endswith('.npy'):
        fd = np.load('./data/'+file)
        face_data.append(fd)
        n = file[:-4]
        name[cid] = n
        face_labels.append(np.ones(fd.shape[0])*cid)
        cid += 1

face_data = np.concatenate(face_data)
face_labels = np.concatenate(face_labels)


clf = KNeighborsClassifier(5)
clf.fit(face_data,face_labels)


while True:
    ret,frame = cap.read()
    
    if ret == False:
        continue

    faces = face_classifier.detectMultiScale(frame,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),[255,0,0],2)
        offset = 10
        face_img = frame[y-offset:y+h+offset, x-offset:x+w+offset]
        face_img = cv2.resize(face_img,(100,100))
        out = clf.predict([face_img.flatten()])[0]
        n = name[out]
        cv2.putText(frame,n,(x,y-offset), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),2,cv2.LINE_AA)
        
    cv2.imshow('Captured Image',frame)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

