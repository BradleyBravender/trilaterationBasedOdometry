import cv2

# Mouse callback function to get the coordinates
def callback(event, x, y, flags, param):
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

    # Set the mouse callback function to capture click events
    cv2.setMouseCallback('image', callback, {'img': img})  # passes img as an argument to the callback function

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Destroy all the windows
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()