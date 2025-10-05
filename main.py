from ultralytics import YOLO

model = YOLO("./model/poki.pt",task="detect")
results = model(source="screen",save=True)
