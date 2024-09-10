import cv2

image = cv2.imread('lane_image.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)