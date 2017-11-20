import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("group.jpg",1)
img = cv2.resize(img, (800, 480))

faces = faceCascade.detectMultiScale(img,scaleFactor=1.1,minSize=(30, 30),minNeighbors=5)	
for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

### Czesc programu sluzaca do wykrywania oczu na obrazie




###

cv2.imshow("Faces found", img)
key = cv2.waitKey(0)


