import cv2
import glob
# Load a cascade file for detecting faces
faceCascade = cv2.CascadeClassifier("/home/wrwr/opencv/data/haarcascades/haarcascade_frontalface_default.xml");

# Load image
#image = cv2.imread("seerde.jpg")


image = []
for img in glob.glob("*.**g"):
    n= cv2.imread(img)
    image.append(n)
    
i = 1
for imgg in image:
    
    # Convert into grayscale
    gray = cv2.cvtColor(imgg, cv2.COLOR_BGR2GRAY)

    # Look for faces in the image using the loaded cascade file
    faces = faceCascade.detectMultiScale(gray, 1.2, 5)
    for (x,y,w,h) in faces:
        # Create rectangle around faces
        cv2.rectangle(imgg,(x,y),(x+w,y+h),(255,255,0),2)
        #rad = int(round((w + h)*0.25))
        #cv2.circle(image,((x + w//2, y + h//2)),(int(rad)),(255,255,0),2)
    st = 'FaceDetection '
    # Create the resizeable window
    cv2.namedWindow(st+str(i), cv2.WINDOW_NORMAL)
    
    # Display the image
   
    cv2.imshow(st+str(i), imgg)
    i = i + 1
    # Wait until we get a key
    k=cv2.waitKey(0)

    # If pressed key is 's'
    if k == ord('s'):
    # Save the image
       # cv2.imwrite('convertedimage.jpg', imgg)
    # Destroy all windows
        cv2.destroyAllWindows()
    # If pressed key is ESC
    elif k == 27:
    # Destroy all windows
        cv2.destroyAllWindows()
    
