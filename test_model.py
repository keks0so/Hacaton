from ultralytics import YOLO
import os
import shutil



model_path = './runs/train8/weights/best.pt'
model = YOLO(model_path)


image = './runs/test_images/fire.mp4'
def detection_and_mention(vid):
    model.predict(source=vid, show=True, conf=0.7, save_crop=True)
    
    
    
