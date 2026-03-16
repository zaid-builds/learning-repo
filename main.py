import cv2

cam = cv2.VideoCapture(0)
fw= int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
fh=int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret,frame=cam.read()
    cv2.imshow('Cam', frame)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()