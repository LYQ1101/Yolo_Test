from ultralytics import YOLO

model=YOLO('yolo12n.pt')

model.train(data='icon.yaml',workers=0,epochs=500,batch=16)