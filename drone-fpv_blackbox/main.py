import cv2
import numpy as np

cap = cv2.VideoCapture(1) # for mac 1
						  # for raspberry 0

width = int(cap.get(3))
height = int(cap.get(4))
fps = 30 


