#!/usr/bin/env python3

import cv2

def process_frame(img):
  print("hello")
  img = cv2.resize(img,(1080//4,1920//4))
  print(img.shape)

if __name__ =="__main__":
  cap = cv2.VideoCapture("drive_view.mp4")
  print("Hello World")
  while cap.isOpened():
    ret, frame = cap.read()
    if ret  == True:
      process_frame(frame)
    else:
      breakap = cv2.VideoCapture("drive_view.mp4")
  print("Hello World")
  while cap.isOpened():
    ret, frame = cap.read()
    if ret  == True:
      process.frame(frame)
    else:
      break
