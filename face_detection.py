import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('img_1.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)


newImg = cv2.resize(img, dsize=(500, 500))

cv2.imshow('img', newImg)
cv2.waitKey()


