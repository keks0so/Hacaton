
from ultralytics import YOLO
model = YOLO("yolov8n.yaml")
results = model.train(data="cocosecure.yaml", epochs=600, device=0)