# basic module load
import cv2
import numpy as np
import time 

# os check for switching 
def os_check():
	''' 
	os_check is check os name and
	if mac return mode 0, linus return mode 1
	'''
	import platform
	os_name = platform.system()

	if os_name == "Darwin":
		mode = 0
	elif os_name == "Linux":
		mode = 1
	else :
		print("sorry not support os type")
	return mode

mode = os_check()
print(f"mode {mode} is selected ")

'''
mode 0  is mac system
mode 1  is Linux system
'''
if mode == 0 :
	cap = cv2.VideoCapture(1) 
	width = int(cap.get(3))  
	height = int(cap.get(4))
	fps = 30 
	fcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")

elif mode == 1:
	cap = cv2.VideoCapture(0) 
	width = int(cap.get(3))
	height = int(cap.get(4))
	fps = 30 
	fcc = cv2.VideoWriter_fourcc(*'XVID')

# writer module file name will be start recording time
name = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
name = name + ".avi"
out = cv2.VideoWriter(name, fcc, fps, (width, height))

while True:
	ret, frame = cap.read()
	
	if mode == 0:	
		cv2.imshow("img", frame)
		out.write(frame)
	else :
		out.write(frame)

	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

cap.release()
