#image read
import cv2 as cv
#img=cv.imread('Photos/cat1.jpg')
#cv.imshow('Cat',img)

#video read

capture=cv.VideoCapture('Videos/video3.mp4')
while True:
    isTrue, frame=capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()