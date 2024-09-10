import cv2
import numpy as np

image = cv2.imread('lane_image.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
backSub = cv2.createBackgroundSubtractorMOG2()
foreground_mask = backSub.apply(blurred_image)
edges = cv2.Canny(blurred_image, 50, 150)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)
lane_image = np.zeros_like(image)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(lane_image, (x1, y1), (x2, y2), (255, 255, 255), 3)