import numpy as np
import cv2

a = '3_cat.mp4'
cam = cv2.VideoCapture(a)

if not cam.isOpened():
  exit()

tracker = cv2.TrackerCSRT_create()
for i in range(80):
 ret, img = cam.read()

cv2.namedWindow('SW')
cv2.imshow('SW', img)

rect = cv2.selectROI('SW', img, fromCenter=False, showCrosshair=True)
cv2.destroyWindow('SW')

tracker.init(img, rect)

while True :
    ret, img = cam.read()

    if not ret :
        exit()

    success, box = tracker.update(img)

    left, top, w, h = [int(v) for v in box]

    cv2.rectangle(img, pt1=(left,top), pt2=(left +w,top +h), color=(255,255,255), thickness=3)

    cv2.imshow('img',img)
    if cv2.waitKey(1) == ord('q'):
        break