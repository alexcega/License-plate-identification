## imports
from ultralytics import YOLO
import cv2

# load models
car_detector = YOLO('yolo11m.pt')
license_plate_detector = YOLO('models/run1_best.pt')

