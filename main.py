import cv2
# print(cv2.__version__)

#Load image ('img name', 0-> greyscale/ 1-> color/ -1 -> alpha channel)
img = cv2.imread('img.png', -1)
# img.set(3, 255)
# print(img)

#show image --> ('window name', 'file name which had to be shown')
cv2.imshow('phIn ala', img)
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    #write image/ create new cv2.imwrite('name', img)
    cv2.imwrite('Grey.png', img)
    cv2.destroyAllWindows()
