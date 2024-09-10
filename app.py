import cv2

image = cv2.imread('lane_image.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
backSub = cv2.createBackgroundSubtractorMOG2()
foreground_mask = backSub.apply(blurred_image)
edges = cv2.Canny(blurred_image, 50, 150)