import numpy as np 
import cv2
cap=cv2.VideoCapture(1)
while(True):
	ret , frame = cap.read()
	gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
	negative = 255 - frame 
	cv2.imshow('frame',frame)
	cv2.imshow('gray',gray)
	cv2.imshow('negative',negative)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
