import cv2
import sys

s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

#Creates a VideoCapture object named 'source' using the camera index s.
source = cv2.VideoCapture(s)

#Sets the window name for displaying the camera feed.
win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

while cv2.waitKey(1) != 27: #  Loops until the 'Esc' key (27) is pressed.
    has_frame, frame = source.read()
    if not has_frame:
        break
    cv2.imshow(win_name, frame) #Displays the current frame in the window.

source.release()
cv2.destroyWindow(win_name) # Destroys the window, freeing up the window resource.


# There are four types of cv2.namedWindow(). They are:-
# 1) cv2.WINDOW_NORMAL: This flag allows the user to resize the window (by dragging its corners or edges).
# 2) cv2.WINDOW_AUTOSIZE: The window size is automatically adjusted to fit the displayed image, and user resizing is not allowed.
# 3) cv2.WINDOW_FULLSCREEN: The window is displayed in fullscreen mode.
# 4) cv2.WINDOW_OPENGL: The window will be created with OpenGL support.
# OpenGL (Open Graphics Library) is a cross-platform API for rendering 2D and 3D vector graphics.