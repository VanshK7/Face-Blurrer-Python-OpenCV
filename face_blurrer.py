import cv2
from cvzone.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture('C:/Users/Vansh/Desktop/Coding/Python/Face Blurrer/demo_video.mp4')

# Initializing Face Detector
detector = FaceDetector(minDetectionCon=0.5)

# Setting maximum window size
MAX_WIDTH = 1000
MAX_HEIGHT = 1000

# Getting video dimensions
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Resizing the window to fit within the maximum dimensions
if width > MAX_WIDTH or height > MAX_HEIGHT:
    if width > height:
        height = int(MAX_WIDTH * height / width)
        width = MAX_WIDTH
    else:
        width = int(MAX_HEIGHT * width / height)
        height = MAX_HEIGHT

# Setting output window size
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", width, height)

while True:
    # Reading the video feed and adding the bounding box to it
    success, img = cap.read()
    img, bboxs = detector.findFaces(img, draw=True)
    
    if bboxs:
        for i, bbox in enumerate(bboxs):
            x,y,w,h=bbox['bbox']            # To get the x, y, width and height of the bounding box for each face
            
            # To prevent out of bounds error
            if x<0: x=0
            if y<0: y=0
            
            imgCrop=img[y:y+h, x:x+h]       # To crop the face from the image
            #cv2.imshow(f"Image Cropped {i}", imgCrop)  
            
            imgBlur=cv2.blur(imgCrop, (101,101))          # To blur the image, give odd values
            img[y:y+h, x:x+w]=imgBlur                   # To put the blurred image on top of the original image

    
    cv2.imshow("Image", img)
    cv2.waitKey(1)

    # Exiting the loop when the video ends
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Releasing the resources
cap.release()
cv2.destroyAllWindows()
