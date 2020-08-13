# OpenCV

![](../.gitbook/assets/image%20%2817%29.png)

With OpenCV on NavQ, you will be able to harness a vast library of computer vision tools for use in HoverGames. OpenCV is installed out of the box on the HoverGames-BSP image and can be installed easily through the package manager on the HoverGames-Demo image. If you'd like to get a jump start on OpenCV, follow the guide below to create a program that detects red objects.

## Quick Example

Let's go through a quick example of running OpenCV on the NavQ to identify a red object in an image taken on the Google Coral camera. This example will be written in Python and uses OpenCV.

![](../.gitbook/assets/image%20%288%29.png)

### Installing OpenCV

If you are using the default OS that is shipped with the NavQ, you can skip this step.

If you're using the HoverGames-Demo image, you'll need to install python3-opencv. To do so, run the following command in your terminal:

```text
$ sudo apt install python3-opencv
```

### Imports

First, create a new python source file \(name it whatever you want!\). We only need two imports for this program: opencv \(cv2\) and numpy. Numpy is used to create arrays of HSV values.

```text
import cv2
import numpy as np
```

### Capturing an image

To capture an image, we must first open a camera object and then read from it.

```text
# Open camera and capture image form it
cap = cv2.VideoCapture(0)
ret,frame = cap.read()
```

### Downsizing the image

To make our OpenCV pipeline run faster, we're going to shrink our image down to 640x480 resolution. This resolution isn't so small that the image quality will be reduced enough to make a difference in detecting objects, but it will make OpenCV process our image much quicker. 

Another pre-processing step that we will run is a box blur. This will get rid of small artifacts in the image that can throw off our pipeline and will make detecting large objects much easier.

```text
# Resize to make processing faster
frame = cv2.resize(frame, (640,480), interpolation = cv2.INTER_AREA)

# Blur image to make contours easier to find
radius = 10
ksize = int(2 * round(radius) + 1)
image = cv2.blur(frame, (ksize, ksize))
```

### Color filtering

In order to find objects that are red in our image, we will apply an HSV filter to the image to create a mask of the color red in the image.

{% hint style="info" %}
The `lower_red` and `upper_red` variables are found by using a program called GRIP. GRIP is a GUI program for OpenCV. It has tons of great features including code generation. To check GRIP out, go to the website [here](https://wpiroboticsprojects.github.io/GRIP/#/).
{% endhint %}

```text
# Convert to HSV color for filtering
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Filter out all colors except red
lower_red = np.array([0,87,211])
upper_red = np.array([36,255,255])

# Create binary mask to detect objects/contours
mask = cv2.inRange(hsv, lower_red, upper_red)
```

### Finding contours

To find the location of the objects in our image, we will find contours in the mask and sort them by total area. This will allow us to filter out smaller objects that we aren't interested in. We will also be able to detect the objects' position in the image and draw a box around them.

```text
# Find contours and sort using contour area
cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
for c in cnts:
    # Once we hit smaller contours, stop the loop
    if(cv2.contourArea(c) < 100):
        break

    # Draw bounding box around contours and write "Red Object" text
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'Red Object', (x,y), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
```

### Storing the generated images

Finally, we will store the images we generated from this program: the mask and the final image with annotations \(bounding box and text\).

```text
# Write images to disk for debugging
cv2.imwrite('thresh.png', mask)
cv2.imwrite('image.png', frame)

# Close camera
cap.release()
```

### Running the code

To run the code, you'll need to use python3. Run the following command \(&lt;file.py&gt; will be the filename that you saved the code to\):

```text
$ python3 <file.py>
```

### Source code

Here is the complete source code if you'd like to run it on your own NavQ as an example:

```text
# Landon Haugh (NXP) 2020

import cv2
import numpy as np

# Load image, grayscale, Gaussian blur, and Otsu's threshold
cap = cv2.VideoCapture(0)
ret,frame = cap.read()

# Resize to make processing faster
frame = cv2.resize(frame, (640,480), interpolation = cv2.INTER_AREA)

# Blur image to make contours easier to find
radius = 10
ksize = int(2 * round(radius) + 1)
image = cv2.blur(frame, (ksize, ksize))

# Convert to HSV color for filtering
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Filter out all colors except red
lower_red = np.array([0,87,211])
upper_red = np.array([36,255,255])

# Create binary mask to detect objects/contours
mask = cv2.inRange(hsv, lower_red, upper_red)

# Find contours and sort using contour area
cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
for c in cnts:
    # Once we hit smaller contours, stop the loop
    if(cv2.contourArea(c) < 100):
        break

    # Draw bounding box around contours and write "Red Object" text
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'Red Object', (x,y), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    
# Write images to disk for debugging
cv2.imwrite('thresh.png', mask)
cv2.imwrite('image.png', frame)

# Close camera
cap.release()
```

