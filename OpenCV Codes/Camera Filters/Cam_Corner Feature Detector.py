import cv2
import sys
import numpy

# FEATURES = 2

feature_params = dict(maxCorners=500, qualityLevel=0.2, minDistance=15, blockSize=9)
s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

win_name = "Corner Feature Detector"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
source = cv2.VideoCapture(s)

while True:
    has_frame, frame = source.read()
    if not has_frame:
        break

    frame = cv2.flip(frame, 1)  # This flips the frame horizontally. The 1 indicates a horizontal flip (around the y-axis).
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(frame_gray, **feature_params)
    if corners is not None:
        for x, y in numpy.float32(corners).reshape(-1, 2):
            cv2.circle(frame, (int(x), int(y)), 10, (0, 255, 0), 1)
    result = frame

    cv2.imshow(win_name, result)

    key = cv2.waitKey(1)
    if key == ord("Q") or key == ord("q") or key == 27:  # Click on "esc" = 27 , Q and q and it will close the window.
        break

source.release()
cv2.destroyWindow(win_name)
