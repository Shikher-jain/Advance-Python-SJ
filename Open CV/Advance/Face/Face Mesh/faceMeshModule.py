import cv2
import time
import mediapipe as mp

class FaceMeshDetector():
    def __init__(self, staticMode=False, maxFaces=6, minDetectionCon=0.5, minTrackCon=0.5):
        self.staticMode = staticMode
        self.maxFaces = maxFaces
        self.minDetectionCon = minDetectionCon
        self.minTrackCon = minTrackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        # self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode, self.maxFaces, self.minDetectionCon, self.minTrackCon)
        self.faceMesh = self.mpFaceMesh.FaceMesh(static_image_mode=self.staticMode,max_num_faces=self.maxFaces,min_detection_confidence=self.minDetectionCon,min_tracking_confidence=self.minTrackCon)

        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)        


    def findFaceMesh(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(imgRGB)

        if self.results.multi_face_landmarks:
            faces = []
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_TESSELATION, self.drawSpec, self.drawSpec)

                face = []
                ih, iw, ic = img.shape
                for id,lm in enumerate(faceLms.landmark):
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    face.append([x,y])
                faces.append(face)
            if draw:
                cv2.putText(img, 'Face Mesh', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
            return img, faces
        else:
            return img, []

    
def main():

    path = r"F:\SHIKHER-VS\Regular\Advance-Python-SJ\Open CV\Advance\Face\Videos\1.mp4"
    cap = cv2.VideoCapture(path)
    cap.set(3, 640)
    cap.set(4, 480)
    pTime = 0

    detector = FaceMeshDetector(maxFaces=10)

    while True:
        # success, img =cap.read()
        img, faces = detector.findFaceMesh(img, draw=True)

        if len(faces) != 0:
            print(faces[0])
            # for face in faces:
            #     for id, lm in enumerate(face):
            #         cv2.putText(img, str(id), (lm[0], lm[1]), cv2.FONT_HERSHEY_PLAIN, 0.7, (255, 0, 0), 1)
            #         cv2.circle(img, (lm[0], lm[1]), 3, (255, 0, 0), cv2.FILLED)
            #         print(id, lm[0], lm[1])


    
        cTime= time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        # cv2.putText(img, f'FPS: {int(fps)}' , (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow("Image", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()