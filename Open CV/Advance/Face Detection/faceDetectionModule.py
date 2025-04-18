import cv2
import mediapipe as mp  
import time

class FaceDetector():

    def __init__(self, minDetectionCon=0.5):
        self.minDetectionCon = minDetectionCon

        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon)

    def findFaces(self,img, draw =True):
        
        img = cv2.flip(img, 1)  # Flip the image horizontally
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.results = self.faceDetection.process(imgRGB)

        # print(self.results.detections)
        bboxes = []
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                self.mpDraw.draw_detection(img, detection)
                bBoxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape

                bbox = int(bBoxC.xmin * iw), int(bBoxC.ymin * ih), \
                    int(bBoxC.width * iw), int(bBoxC.height * ih)
                
                bboxes.append([id, bbox, detection.score])
                if draw:
                    img = self.fancyDraw(img, bbox)
                    cv2.putText(img, f"{str(int(detection.score[0]*100)) }%", (bbox[0],bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 2,(255,0,255),2)                
        
        return img , bboxes
    
    def fancyDraw(self, img, bbox, l=30, t=10, rt=1,c=(255, 0, 255)):    
        x, y, w, h = bbox
        x1, y1 = x + w, y + h
        
        cv2.rectangle(img, bbox, c , rt)
    
        cv2.line(img, (x, y), (x + l, y),     c , t)       #Top Left to Top Right       color : Yellow
        cv2.line(img, (x, y), (x, y + l),     c , t)       #Top Left to Bottom Left     color : Cyan
        cv2.line(img, (x1, y), (x1 - l, y),   c , t)         #Top Right to Top Left       color : Black  
        cv2.line(img, (x1, y), (x1, y + l),   c , t)   #Top Right to Bottom Right   color : White
        cv2.line(img, (x, y1), (x + l, y1),   c , t)       #Bottom Left to Bottom Right color : Red  
        cv2.line(img, (x, y1),  (x, y1 - l),   c , t)       #Bottom Left to Top Left     color : Green
        cv2.line(img, (x1, y1), (x1 - l, y1), c , t)     #Bottom Right to Bottom Left color : Blue
        cv2.line(img, (x1, y1), (x1, y1 - l), c , t)   #Bottom Right to Top Right   color : Magenta
    
        return img

def main():
    pTime = 0
    cap =cv2.VideoCapture(0)

    detector = FaceDetector()
    
    while True:
        success, img = cap.read()

        img, bboxs = detector.findFaces(img)

        
        if not success:
            break

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime

        cv2.putText(img, f"FPS:{str(int(fps))}", (30, 50), cv2.FONT_HERSHEY_PLAIN, 3,(0,0,255), 3)
        cv2.imshow("Image", img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



if __name__ == "__main__":
    main()