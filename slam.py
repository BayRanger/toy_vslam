#!/usr/bin/env python3
import cv2
#import sdl2.ext

scale = 4
H = 1080//scale
W = 1920//scale

def process_frame(img):
    #print("proces img")
    img = cv2.resize(img,(W,H))
    #events = sdl2.ext.get_events()
    cv2.imshow("image",img)
    #window.refresh()


if __name__ =="__main__":
    cap = cv2.VideoCapture("test.mp4")
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")
    while cap.isOpened():
        ret,frame = cap.read()
        if ret==True:
            process_frame(frame)
            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
    

