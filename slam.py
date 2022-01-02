#!/usr/bin/env python3
import cv2
import time
import sdl2
from display import Display

scale = 4
H,W = 1080//scale, 1920//scale
	
disp = Display(W,H)
\
def process_frame(img):
	img = cv2.resize(img,(W,H))
	disp.paint(img)
if __name__ =="__main__":
	cap = cv2.VideoCapture("test.mp4")
	while cap.isOpened():
		ret,frame = cap.read()
		if ret==True:
			process_frame(frame)
		else:
			break

