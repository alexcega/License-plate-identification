## imports
from ultralytics import YOLO
import cv2

# load models
car_detector = YOLO('yolo11m.pt')
license_plate_detector = YOLO('models/run1_best.pt')

# load video
cap = cv2.VideoCapture('videos/cars.mp4') # TODO add video path

# read frames
ret = True

vehicles  = [2,3,5,7]  # car, motorcycle, bus, truck in COCO dataset

# TODO add video data
while ret:
    frame_nmr += 1 
    ret, frame = cap.read()

    # detect vehicles
    detection = car_detector(frame)[0]
    detect
