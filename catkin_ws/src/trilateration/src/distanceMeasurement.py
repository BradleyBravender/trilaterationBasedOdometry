# The idea in this node to is calculate the distance between the 

import cv2
import sys
import numpy as np
import time

class DistanceNode():
    MIN_RADIUS = 5
    MAX_RADIUS = 1000 # was 20
    SENSITIVITY = 5  # The smaller, the more circles may get detected
    
    def __init__(self):
        cameraNumber = 0
        self.cap = cv2.VideoCapture(cameraNumber)
        if not self.cap.isOpened():
            print("Error: Could not open webcam.")
            exit()
            
      
    # def tune_color(self):


    def get_bounding_box(self):
        success, image = self.cap.read()

        while not success:  
            print(f"Port {cameraNumber} is not connected to a camera. Try a different camera port")
            cameraNumber = int(input("Try a different camera number: "))
            cap = cv2.VideoCapture(cameraNumber)
            success, image = self.cap.read()
        
        # TODO: Tune these parameters:
        # H: Red: (0 and 179), Yellow (30, etc)
        # S: 0 is dull (gray), 255 is vivid
        # V: 0 is dark colors, 255 is bright colors
        lower_color = np.array([0, 120, 0])  # Lower HSV bound for blue
        upper_color = np.array([10, 255, 255])  # Upper HSV bound for blue
        hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        # Process the colors to extract a white and black frame of the color
        mask = cv2.inRange(hsvImage, lower_color, upper_color)
        # Makes the target color black and all other colors white
        invertedMask = cv2.bitwise_not(mask)
        # Create an all-white image
        whiteBackground = np.ones_like(image) * 255
        # Apply the inverted mask to the white background
        filteredFrame = cv2.bitwise_and(whiteBackground, whiteBackground, mask=invertedMask)
        filteredFrame = cv2.medianBlur(filteredFrame, 5)
        filteredFrame = cv2.cvtColor(filteredFrame, cv2.COLOR_BGR2GRAY)

        # Idea: calculate the ceontroid of filteredFrame to help the transform
        # select the closest circle 
        black_pixels = np.where(filteredFrame == 0)

        if black_pixels[0].size > 0:
            centroid_x = np.mean(black_pixels[1])
            centroid_y = np.mean(black_pixels[0])

            # Draw centroid
            cv2.circle(image, (int(centroid_x), int(centroid_y)), 5, (0, 0, 255), -1)

        circles = cv2.HoughCircles(filteredFrame, 
                                   cv2.HOUGH_GRADIENT, 
                                   1, 
                                   20, 
                                   param1=100, 
                                   param2 = self.SENSITIVITY, 
                                   minRadius = self.MIN_RADIUS, 
                                   maxRadius = self.MAX_RADIUS)
        
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")

            # circle = max(circles, key=lambda c: c[2])
            # x = int(circle[0])
            # y = int(circle[1])
            # cv2.circle(image, (x, y), 1, (0, 255, 0), 1)

            x, y, r = circles[0]
            
            topLeft = (x - r, y - r)
            topRight = (x + r, y - r)
            bottomLeft = (x - r, y + r)
            bottomRight = (x + r, y + r)
                
            cv2.circle(image, topLeft, 3, (0, 255, 0), 1)
            cv2.circle(image, topRight, 3, (0, 255, 0), 1)
            cv2.circle(image, bottomLeft, 3, (0, 255, 0), 1)
            cv2.circle(image, bottomRight, 3, (0, 255, 0), 1)
            cv2.circle(image, (x,y), 3, (0, 255, 0), 1)
            
        
        # Display the original and filtered frames
        cv2.imshow('Original Webcam Feed', image)
        cv2.imshow('Filtered Webcam Feed', filteredFrame)  # For Debugging

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.shutdown()


    # def get_distance(self, x, y, w, h):
        
    #     pass


    def shutdown(self):
        self.cap.release()
        cv2.destroyAllWindows()


if __name__=="__main__":
    distanceDetector = DistanceNode()
    while True:
        distanceDetector.get_bounding_box()

    
