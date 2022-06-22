import numpy as np
import cv2

img = np.ones((400, 400, 3))
img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 5)
cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()