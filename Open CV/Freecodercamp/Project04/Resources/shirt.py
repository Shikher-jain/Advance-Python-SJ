import os
import cvzone
import cv2
from cvzone.PoseModule import PoseDetector

# Video Path

# Videopath = "F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Project04/Resources/Videos/1.mp4"
# cap = cv2.VideoCapture(Videopath)

# Webcam Setup
cap = cv2.VideoCapture(0)
detector = PoseDetector()

# Shirt Folder
shirtFolderPath = "F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Project04/Resources/Shirts"
listShirts = os.listdir(shirtFolderPath)
print("Available Shirts:", listShirts)

# Constants
fixedRatio = 262 / 190  # widthOfShirt / widthOfPoint11to12
shirtRatioHeightWidth = 581 / 440
imageNumber = 0
imgButtonRight = cv2.imread("F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Project04/Resources/button.png", cv2.IMREAD_UNCHANGED)
imgButtonLeft = cv2.flip(imgButtonRight, 1)
counterRight = 0
counterLeft = 0
selectionSpeed = 10

# ✅ Set Full Screen Window
cv2.namedWindow("Image", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    success, img = cap.read()
    if not success:
        print("Video Read Error or End of Video")
        break
    
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)

    if lmList:
        lm11 = lmList[11][1:3]
        lm12 = lmList[12][1:3]

        # Load Shirt Image
        imgShirt = cv2.imread(os.path.join(shirtFolderPath, listShirts[imageNumber]), cv2.IMREAD_UNCHANGED)

        # Width Calculation (Fixed Negative/Zero Issue)
        widthOfShirt = max(1, int(abs(lm11[0] - lm12[0]) * fixedRatio))
        heightOfShirt = max(1, int(widthOfShirt * shirtRatioHeightWidth))

        # Resize Shirt
        imgShirt = cv2.resize(imgShirt, (widthOfShirt, heightOfShirt))

        # Offset Calculation
        currentScale = (abs(lm11[0] - lm12[0])) / 190
        offset = int(44 * currentScale), int(48 * currentScale)

        # Overlay Shirt on Image
        try:
            img = cvzone.overlayPNG(img, imgShirt, (lm12[0] - offset[0], lm12[1] - offset[1]))
        except Exception as e:
            print("Error overlaying shirt:", e)

        # Overlay Buttons
        img = cvzone.overlayPNG(img, imgButtonRight, (1074, 293))
        img = cvzone.overlayPNG(img, imgButtonLeft, (72, 293))

        # Shirt Selection Logic
        if lmList[16][1] < 300:
            counterRight += 1
            cv2.ellipse(img, (139, 360), (66, 66), 0, 0, counterRight * selectionSpeed, (0, 255, 0), 20)
            if counterRight * selectionSpeed > 360:
                counterRight = 0
                if imageNumber < len(listShirts) - 1:
                    imageNumber += 1
        elif lmList[15][1] > 900:
            counterLeft += 1
            cv2.ellipse(img, (1138, 360), (66, 66), 0, 0, counterLeft * selectionSpeed, (0, 255, 0), 20)
            if counterLeft * selectionSpeed > 360:
                counterLeft = 0
                if imageNumber > 0:
                    imageNumber -= 1
        else:
            counterRight = 0
            counterLeft = 0

    # Show Full-Screen Output
    cv2.imshow("Image", img)

    # Press "Q" to Quit
    key = cv2.waitKey(1)
    if key == ord('q'):  # 'q' dabane par exit
        print("Q pressed! Exiting...")
        break

# Proper Cleanup
cap.release()  # Video capture release
cv2.destroyAllWindows()  # Close all OpenCV windows
