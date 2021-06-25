import cv2
import numpy as np
import time 

cap = cv2.VideoCapture(0) # for mac 1
						  # for raspberry 0

width = int(cap.get(3))
height = int(cap.get(4))
fps = 30 

fcc = cv2.VideoWriter_fourcc("M", "J", "P", "G") # for mac fourcc 
												 # for raspberry pi 
												 # cv2.VideoWriter_fourcc(*'XVID')

# writer module file name will be start recording time
name = time.strftime('%c', time.localtime(time.time()))
name = name + ".avi"
out = cv2.VideoWriter(name, fcc, fps, (width, height))

while True:
	ret, frame = cap.read()
	cv2.imshow("img", frame)
	out.write(frame) 
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

cap.release()