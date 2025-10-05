这是一个YOLO的学习过程项目


项目模型来源网址：https://docs.ultralytics.com/zh/


项目解释：
model目录下是使用的模型来源
datesets中images是待标注的图片，train是训练集，val是验证集
labels中对应的是在labelimg中标注后得到的yolo对应的文本

runs中存储训练验证和测试验证结果
detect下predict是储存测试后的结果，trianx代表训练好的模型，x越大效果越好，其下的weight中的best.pt就是模型

train.py进行训练

main.py是测试训练好的模型测试文件
test用来存储测试数据

注意调整icon.yaml中的参数