from ultralytics import YOLO
import os


model_path = "E:/Work/JUPYTER/Security/runs/detect/train/weights/best.pt"
model = YOLO(model_path)
model.predict(source="fire.mp4", show=True, conf=0.6)