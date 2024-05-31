import cv2
import sys

# BLUR = 1

s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

win_name = "Blurring Filter"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
source = cv2.VideoCapture(s)

while True:
    has_frame, frame = source.read()
    if not has_frame:
        break

    frame = cv2.flip(frame, 1)  # This flips the frame horizontally. The 1 indicates a horizontal flip (around the y-axis).
    result = cv2.blur(frame, (13, 13))

    cv2.imshow(win_name, result)

    key = cv2.waitKey(1)
    if key == ord("Q") or key == ord("q") or key == 27:  # Click on "esc" = 27 , Q and q and it will close the window.
        break

source.release()
cv2.destroyWindow(win_name)







