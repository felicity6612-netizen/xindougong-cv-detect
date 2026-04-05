# xindougong-cv-detect
新斗拱构件缺陷检测工具 / OpenCV-based component defect detection
# 新斗拱构件缺陷检测工具

基于 OpenCV 的建筑构件缺陷检测脚本，用于「新斗拱」文创产品的品控迭代。

## 功能
- 输入构件图片，自动提取边缘轮廓
- 对形状比例异常区域进行红框标注
- 输出检测到的问题数量

## 使用方法
1. 将待检测图片命名为 `test.jpg` 放入同目录
2. 运行 `python detect.py`
3. 查看弹出的 Original / Edges / Result 三个窗口

## 依赖
pip install opencv-python numpy
