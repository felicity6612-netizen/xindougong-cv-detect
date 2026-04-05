import cv2
import numpy as np

# 读取图片
img = cv2.imread("test2.png")
output = img.copy()

# 转灰度
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 高斯模糊（去噪）
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 边缘检测
edges = cv2.Canny(blur, 50, 150)

# 查找轮廓
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 设定面积阈值（过滤噪声）
min_area = 100

problem_count = 0

for cnt in contours:
    area = cv2.contourArea(cnt)

    if area > min_area:
        # 计算外接矩形
        x, y, w, h = cv2.boundingRect(cnt)

        # 简单规则：形状异常（过细 or 过扁）
        aspect_ratio = w / h if h != 0 else 0

        if aspect_ratio < 0.3 or aspect_ratio > 3:
            # 标记问题区域
            cv2.rectangle(output, (x, y), (x + w, y + h), (0, 0, 255), 2)
            problem_count += 1
        else:
            # 正常区域
            cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 1)

# 输出结果
cv2.putText(output, f"Problems detected: {problem_count}",
            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow("Original", img)
cv2.imshow("Edges", edges)
cv2.imshow("Result", output)

cv2.waitKey(0)
cv2.destroyAllWindows()