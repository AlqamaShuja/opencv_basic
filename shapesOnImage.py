import numpy as np
import cv2

img = cv2.imread('img.png', 1)
img = np.zeros([700, 700, 3], np.uint8)

#     cv2.line(img, (startX, startY), (endX, endY), (Blue, Green, Red), thickness)
img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 5)
img = cv2.arrowedLine(img, (0, 255), (255, 255), (245, 221, 66), 3)
img = cv2.rectangle(img, (540, 0), (340, 100), (128, 65, 91), 3)
img = cv2.circle(img, (320, 50), 20, (108, 10, 233), -1)

# Text on Image
font = cv2.FONT_HERSHEY_SIMPLEX
# img = cv2.putText(img, 'OpenCV', (startX, startY), font, fontSize, (255, 255, 255), 10, cv2.LINE_AA)
img = cv2.putText(img, 'OpenCV', (10, 400), font, 4, (255, 255, 255), 10, cv2.LINE_AA)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()