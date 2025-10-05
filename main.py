from ultralytics import YOLO

model = YOLO("./model/yolo12l.pt",task="detect")
results = model(source="screen",save=True)
