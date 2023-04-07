# Face-Blurrer-Python-OpenCV
Python script that detects faces in video using OpenCV &amp; cvzone, blurs them out in real-time, and overlays them onto the original image. Useful for anonymizing people in videos for privacy reasons. Demo video included.

## Requirements
*Python 3.x*
*OpenCV*
*cvzone*

## Usage
1. Import the necessary libraries:
```
import cv2
from cvzone.FaceDetectionModule import FaceDetector
```
2. Load the video to be processed:
`cap = cv2.VideoCapture('path/to/input/video.mp4')`
3. Initialize the face detector:
`detector = FaceDetector(minDetectionCon=0.5)`
4. Set the maximum window size and get the video dimensions:
```
MAX_WIDTH = 1000
MAX_HEIGHT = 1000

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
```
5. Resize the window to fit within the maximum dimensions:
```
if width > MAX_WIDTH or height > MAX_HEIGHT:
    if width > height:
        height = int(MAX_WIDTH * height / width)
        width = MAX_WIDTH
    else:
        width = int(MAX_HEIGHT * width / height)
        height = MAX_HEIGHT
```
6. Iterate over each frame of the video, detect the faces and apply the blur effect:
```
while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img, draw=True)
    
    if bboxs:
        for i, bbox in enumerate(bboxs):
            x,y,w,h=bbox['bbox']
            
            if x<0: x=0
            if y<0: y=0
            
            imgCrop=img[y:y+h, x:x+h]
            imgBlur=cv2.blur(imgCrop, (101,101))
            img[y:y+h, x:x+w]=imgBlur

    out.write(img)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```
7. Release the resources:
```
cap.release()
cv2.destroyAllWindows()
```
