from ultralytics import YOLO

model = YOLO("yolo12n.pt",task="detect")
results = model(source="test/2.jpg",save=True)
