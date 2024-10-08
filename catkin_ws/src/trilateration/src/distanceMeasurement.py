###############################################################################
# *Author*:     Bradley Bravender
# *Purpose*:    This node calculates the distance between the given camera and 
#               the object.   
# *To Do*       Integrate ROS in order to have this node publish the distance
#               between the object and the camera.
###############################################################################

import argparse
import cv2
import sys
import numpy as np
import time

class DistanceNode():   
    def __init__(self, args):
        """
        Initializes the distance class, which estimates the distance between
        the object and the camera.

        Parameters
        ----------
        args : argparse.ArgumentParser
            Used to pass parameters to the Hough transform
        """
        self.minRadius = args.minRadius
        self.maxRadius = args.maxRadius
        # The smaller the sensitivity, the more circles may get detected.
        self.sensitivity = args.sensitivity
        cameraNumber = 0
        self.distanceBuffer = []
        self.cap = cv2.VideoCapture(cameraNumber)
        if not self.cap.isOpened():
            print("Error: Could not open webcam.")
            exit()
            

    def get_bounding_box(self):
        """
        Uses color filtering and a hough transform to draw a bounding box around
        the object.
        """
        success, image = self.cap.read()

        while not success:  
            print(f"Port {cameraNumber} is not connected to a camera.")
            print("Try a different camera port")
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
        filteredFrame = cv2.bitwise_and(
            whiteBackground, 
            whiteBackground, 
            mask=invertedMask
        )
        filteredFrame = cv2.medianBlur(filteredFrame, 5)
        filteredFrame = cv2.cvtColor(filteredFrame, cv2.COLOR_BGR2GRAY)

        # Idea: calculate the centroid of filteredFrame to help the transform
        # select the closest circle 
        black_pixels = np.where(filteredFrame == 0)

        if black_pixels[0].size > 0:
            centroid_x = np.mean(black_pixels[1])
            centroid_y = np.mean(black_pixels[0])

            # Draw centroid
            cv2.circle(
                image, 
                (int(centroid_x), 
                 int(centroid_y)), 
                 5, 
                 (0, 0, 255), 
                 -1
            )

        circles = cv2.HoughCircles(
            filteredFrame, 
            cv2.HOUGH_GRADIENT, 
            1, 
            20, 
            param1=100, 
            param2 = self.sensitivity, 
            minRadius = self.minRadius, 
            maxRadius = self.maxRadius
        )
        
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")

            # circle = max(circles, key=lambda c: c[2])
            # x = int(circle[0])
            # y = int(circle[1])
            # cv2.circle(image, (x, y), 1, (0, 255, 0), 1)

            x, y, r = circles[0]

            self.get_distance(2 * r)
            
            # TODO: turn the code below into its own visualization method.
            # For visualization:

            visual = False
            if visual:
                topLeft = (x - r, y - r)
                topRight = (x + r, y - r)
                bottomLeft = (x - r, y + r)
                bottomRight = (x + r, y + r)
                    
                cv2.circle(filteredFrame, topLeft, 3, (0, 255, 0), 1)
                cv2.circle(filteredFrame, topRight, 3, (0, 255, 0), 1)
                cv2.circle(filteredFrame, bottomLeft, 3, (0, 255, 0), 1)
                cv2.circle(filteredFrame, bottomRight, 3, (0, 255, 0), 1)
                cv2.circle(filteredFrame, (x,y), 3, (0, 255, 0), 1)            
        
                # Display the original and filtered frames
                # cv2.imshow('Original Webcam Feed', image)

                # For Debugging
                cv2.imshow('Filtered Webcam Feed', filteredFrame)  

                # Break the loop when 'q' key is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.shutdown()


    def get_distance(self, pixelHeight):
        """
        Uses optics math and the estimated height of the object to calculate 
        predicted distance between the object and the camera.

        Parameters
        ----------
        pixelHeight : int
            The height of the object in pixels.
        """
        actualHeight = 0.111  # meters
        focalLength = 1845       # TODO: calculate a more accurate focal length  
        distance = (focalLength * actualHeight) / pixelHeight
        # distance = int(input("distance in cm: "))/100
        # focalLength = (pixelHeight * distance) / actualHeight
        
        if len(self.distanceBuffer) > 2:
            self.distanceBuffer.pop(0)
        
        self.distanceBuffer.append(distance)
        
        # Take the average distance
        finalDistance = sum(self.distanceBuffer) / len(self.distanceBuffer)
        print(f"Distance from camera: {(finalDistance):.2f} meters.")
        

    def shutdown(self):
        """
        Shuts everything down. Add a ROS node shutdown call once ROS is 
        integrated.
        """
        self.cap.release()
        cv2.destroyAllWindows()


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Description of your program")
    parser.add_argument(
        '--minRadius', 
        type=int, 
        help='Minimum circle radius to detect', 
        default=5
    )
    parser.add_argument(
        '--maxRadius', 
        type=int, 
        help='Maximum circle radius to detect', 
        default=1000
    )
    parser.add_argument(
        '--sensitivity', 
        type=int, 
        help='Sensitivity of the transform', 
        default=20
    )
    args = parser.parse_args()
    
    distanceDetector = DistanceNode(args)
    while True:
        distanceDetector.get_bounding_box()