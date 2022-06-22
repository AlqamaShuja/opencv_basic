# Normal Capturing
import cv2
# // Shehroz, saqib
cap = cv2.VideoCapture(0)
# address = "http://192.168.1.101:8080/video"
address = "http://192.168.1.101:4747/video"
# cap.read(address)

while True:
    ret, frame = cap.read(address)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# Gray Scale Capturing
# import cv2
#
# cap = cv2.VideoCapture(0);
#
# while(cap.isopened()):
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('frame', gray)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()


# Save Capturing Video
# import cv2
#
# cap = cv2.VideoCapture(0);
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
#       #cv2.VideoWriter('Video name', Video Code (fourcc.org), no of frame, (width, height))
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
#
# while(cap.isopened()):
#     ret, frame = cap.read()    #ret is true if frame is available
#
#     if ret ==True:
#         #width, height of frame
#         print(cap.get(cv2.CAP_PROP_FRAME_WIDTH));
#         print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT));
#
#         out.write(frame)
#
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         cv2.imshow('frame', gray)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
#
#
# cap.release()
# out.release()
# cv2.destroyAllWindows()
