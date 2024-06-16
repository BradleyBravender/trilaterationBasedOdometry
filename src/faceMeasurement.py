import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(3)  # the camera to select

while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)

# cap = cv2.VideoCapture(2)  # the camera to select
# detector = FaceMeshDetector(maxFaces=1)
# while True:
#     success, img = cap.read()
#     img, faces = detector.findFaceMesh(img, draw=False)

#     if faces:
#         face = faces[0]
#         pointLeft = face[145]
#         pointRight = face[374]
#         cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)
#         cv2.circle(img, pointLeft, 5, (255, 0, 255), cv2.FILLED)
#         cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)
#         w, _ = detector.findDistance(pointLeft, pointRight)
        
#         # to find the focal length
#         W = 6.3 # average distance in cm between pupils
#         d = 50
#         f = (w*d)/W
#         print(w)

#     #print(f"success {success}, img {img}")
#     cv2.imshow("Image", img)
#     cv2.waitKey(1)


    
