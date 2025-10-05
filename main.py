from ultralytics import YOLO

model = YOLO("./model/huishouzhan.pt",task="detect")
results = model(source="screen",save=True)
