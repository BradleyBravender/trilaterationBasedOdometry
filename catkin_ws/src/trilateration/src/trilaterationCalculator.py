###############################################################################
# *Author*:     Bradley Bravender
# *Purpose*:    This script takes the distance between all cameras and the 
#               object, as well as the camera positions relative to the world 
#               map, in order to trilaterate and visually display the objects
#               predicted position.    
# *To Do*       Have this script read the camera position file generated by 
#               `cameraCalibration.py`. Have it subscribe to the ROS topic(s)
#               associated with the distance to the cameras at any given time. 
###############################################################################

import numpy as np
import matplotlib.pyplot as plt
import time


def draw_circle(array, center, radius):
    """
    Takes the camera position and distance from the object and plots a circle
    representing all possible positions the object may be with respect to the 
    camera.

    Parameters
    ----------
    array : ndarray
        A blank array of the size of the pixel width and height of the world 
        map image.
    center : int
        The camera position with respect to the world map. 
    radius : int
        The distance between the camera and the object

    Returns
    -------
    ndarray
        An array of the same dimensions as the world map, with all possible 
        positions of the world map displayed within it. 
    """
    matrix = array.copy()
    cx, cy = center
    rows, cols = matrix.shape
    radius = radius + 40  # Inflate the radius to equal the size of the outermost ring
    # TODO: Radius inflation parameter needs tuning
    # The following loop adds an inflated radius to account for distance errors. 
    for x in range(cx - radius, cx + radius + 1):
        for y in range(cy - radius, cy + radius + 1):
            if 0 <= x < rows and 0 <= y < cols:
                if round((x - cx) ** 2 + (y - cy) ** 2) <= (radius) ** 2:
                    matrix[x, y] = 1
                if round((x - cx) ** 2 + (y - cy) ** 2) <= (radius - 10) **2:
                    matrix[x, y] = 2
                if round((x - cx) ** 2 + (y - cy) ** 2) <= (radius - 20) ** 2:
                    matrix[x, y] = 3
                if round((x - cx) ** 2 + (y - cy) ** 2) <= (radius - 30) **2:
                    matrix[x, y] = 2
                if round((x - cx) ** 2 + (y - cy) ** 2) <= (radius - 40) ** 2:
                    matrix[x, y] = 1
                if round((x - cx) ** 2 + (y - cy) ** 2) <= (radius - 50) **2:
                    matrix[x, y] = 0
    return matrix


if __name__=="__main__":
    rows = 1080
    cols = 1920
    startTime = time.time()
    array = np.zeros((rows, cols), dtype=int)
    print(f"Drawing circle 1. Elapsed time: {((time.time() - startTime)*1000):.2f} ms")
    array_1 = draw_circle(array, (300, 300), 141)
    print(f"Drawing circle 2. Elapsed time: {((time.time() - startTime)*1000):.2f} ms")
    array_2 = draw_circle(array, (600, 600), 565)
    print(f"Drawing circle 3. Elapsed time: {((time.time() - startTime)*1000):.2f} ms")
    array_3 = draw_circle(array, (500, 1000), 851)
    print(f"Summing array layers. Elapsed time: {((time.time() - startTime)*1000):.2f} ms")
    array = np.sum([array_1, array_2, array_3], axis=0)

    plt.imshow(array, cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.show()