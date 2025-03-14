import cv2
import time
import math
import numpy as np
import HandTrackingModule as htm
import pyautogui

try:
    import autopy
except ImportError:
    autopy = None  # Use pyautogui if autopy fails

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Camera settings
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0
detector = htm.handDetector(maxHands=1, detectionCon=0.85, trackCon=0.8)

# Audio control setup
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol, maxVol = volRange[0], volRange[1]
volBar, volPer, vol = 400, 0, 0

# Other configurations
tipIds = [4, 8, 12, 16, 20]
mode = ''
active = 0
pyautogui.FAILSAFE = False

# Function to display text on screen
def putText(img, mode, loc=(250, 450), color=(0, 255, 255)):
    cv2.putText(img, str(mode), loc, cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, color, 3)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    fingers = []

    if lmList:
        # Thumb Detection (Left vs Right hand logic)
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:  
            fingers.append(1)
        else:
            fingers.append(0)

        # Other Fingers
        for id in range(1, 5):
            fingers.append(1 if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2] else 0)

        # Mode Selection
        if fingers == [0, 0, 0, 0, 0] and active == 0:
            mode = 'N'
        elif fingers in [[0, 1, 0, 0, 0], [0, 1, 1, 0, 0]] and active == 0:
            mode = 'Scroll'
            active = 1
        elif fingers == [1, 1, 0, 0, 0] and active == 0:
            mode = 'Volume'
            active = 1
        elif fingers == [1, 1, 1, 1, 1] and active == 0:
            mode = 'Cursor'
            active = 1

    # Scroll Mode
    if mode == 'Scroll':
        putText(img, mode)
        if fingers == [0, 1, 0, 0, 0]:
            putText(img, 'U', loc=(200, 455), color=(0, 255, 0))
            pyautogui.scroll(50)
        elif fingers == [0, 1, 1, 0, 0]:
            putText(img, 'D', loc=(200, 455), color=(0, 0, 255))
            pyautogui.scroll(-50)
        elif fingers == [0, 0, 0, 0, 0]:
            active = 0
            mode = 'N'

    # Volume Mode
    if mode == 'Volume':
        putText(img, mode)

        if fingers[-1] == 1:
            active = 0
            mode = 'N'

        else:
            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[8][1], lmList[8][2]
            length = math.hypot(x2 - x1, y2 - y1)
            vol = np.interp(length, [50, 200], [minVol, maxVol])
            volBar = np.interp(vol, [minVol, maxVol], [400, 150])
            volPer = np.interp(vol, [minVol, maxVol], [0, 100])

            volume.SetMasterVolumeLevel(vol, None)

            cv2.rectangle(img, (30, 150), (55, 400), (209, 206, 0), 3)
            cv2.rectangle(img, (30, int(volBar)), (55, 400), (215, 255, 127), cv2.FILLED)
            cv2.putText(img, f'{int(volPer)}%', (25, 430), cv2.FONT_HERSHEY_COMPLEX, 0.9, (209, 206, 0), 3)

    # Cursor Mode
    if mode == 'Cursor' and autopy:
        putText(img, mode)
        x1, y1 = lmList[8][1], lmList[8][2]
        w, h = autopy.screen.size()
        X = int(np.interp(x1, [110, 620], [0, w - 1]))
        Y = int(np.interp(y1, [20, 350], [0, h - 1]))
        autopy.mouse.move(X, Y)

    # FPS Calculation
    cTime = time.time()
    fps = 1 / ((cTime + 0.01) - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS:{int(fps)}', (480, 50), cv2.FONT_ITALIC, 1, (255, 0, 0), 2)
    cv2.imshow('Hand LiveFeed', img)

    if cv2.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv2.destroyAllWindows()