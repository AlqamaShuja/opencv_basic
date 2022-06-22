import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
address = "https://192.168.1.101:4747/video"
while True:
    ret, frame = cap.read(address)
    vidGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = face_cascade.detectMultiScale(vidGray, 1.1, 4)

    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('img', frame)
    k = cv2.waitKey(30)

    if k == 27:
        break

cap.release()
# cap.destroyAllWindow()
# newImg = cv2.resize(img, dsize=(500, 500))
