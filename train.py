from ultralytics import YOLO

model=YOLO('./model/yolo12l.pt')

# 指定 device=0 来使用第一块 GPU
model.train(data='icon.yaml', workers=0, epochs=500, batch=4, device=0)