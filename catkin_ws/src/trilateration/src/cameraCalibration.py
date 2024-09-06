###############################################################################
# *Author*:     Bradley Bravender
# *Purpose*:    This script takes an overhead drone image of the camera setup, 
#               and allows the user to select where the cameras are in relation
#               to each other in order to establish their relation relative to 
#               each other.   
# *To Do*       Have the script prompt the user for however many cameras are in 
#               the scene. Add a feature to remove cameras (if the user 
#               incorrectly clicks. Store the camera positions in a pkl file
#               so they can be accessed by other scripts.
###############################################################################

import cv2

# TODO: finish this docstring
def callback(event, x, y, param):
    """
    This callback function draws where the user clicks on the image.

    Parameters
    ----------
    event : _type_
        _description_
    x : int
        The x coordinate of where the user clicked.
    y : int
        The y coordinate of where the user clicked.
    param : _type_
        _description_
    """
    img = param['img']  # receives img as a parameter
    try:
        if event == cv2.EVENT_MBUTTONDOWN:
            print(f"Clicked at: ({x}, {y})")
            # You can also display the coordinates on the image window
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, f"{x}, {y}", (x+15, y), font, 0.5, (255, 0, 0), 2)
            cv2.circle(img, (x, y), 10, (0, 255, 0))
            cv2.circle(img, (x, y), 1, (0, 255, 0), thickness=-1)
            cv2.imshow('image', img)
    except:
        exit(1)
 

def main():
    # Load an image
    img = cv2.imread('testImage.png', 1)

    # Display the image
    cv2.imshow('image', img)

    # Set the mouse callback function to capture click events.
    
    # Passes img as an argument to the callback function.
    cv2.setMouseCallback('image', callback, {'img': img})  
    # Wait until a key is pressed.
    cv2.waitKey(0)

    # Destroy all the windows.
    cv2.destroyAllWindows()


if __name__=="__main__":
    main()