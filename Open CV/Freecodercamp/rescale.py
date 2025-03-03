# aa 111

import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width  = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions)

path="https://v.ftcdn.net/01/94/19/23/700_F_194192359_wP4uCWZ5ruMIBAkGq5sKRRGduae5SQmE_ST.mp4"
capture = cv.VideoCapture(path)

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow("Original", frame)
    cv.imshow("Resized", frame_resized)

    if cv.waitKey(30) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()