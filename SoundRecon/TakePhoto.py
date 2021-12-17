import cv2
from datetime import datetime
import os




def take_photo():
    # now = datetime.now()
     counter = 0
     os.system("raspistill -o images/" +str(counter) +".jpg")
     photoLocation = "images/"+str(counter)+".jpg"
     photo = cv2.imread(photoLocation)
     scale_percent = 30 # percent of original size
     width = int(photo.shape[1] * scale_percent / 100)
     height = int(photo.shape[0] * scale_percent / 100)
     dim = (width, height)
     finalPhoto = cv2.resize(photo, dim, interpolation = cv2.INTER_AREA)
     counter = counter + 1
     cv2.imwrite(photoLocation, finalPhoto)
    #image = cv2.imread(args["images/testimage1.jpg"])
    #cv2.imshow('Imagetest',image)
    #cam = cv2.VideoCapture(0)
    #while True:
        #cnt=0;
        #ret, image = cam.read()
        #cv2.imshow('Imagetest',image)
        #key = cv2.waitKey(27)
        #if (key == 32): #press 'space' to take the photo
         #   cnt=cnt +1
         #   cv2.imwrite('/home/pi/Desktop/SoundRecon/images/testimage' +str(cnt) + ".jpg", image)
        #elif (key == 113): #press 'q' to quit the window
         #   break
    #    cam.release()
    #    cv2.destroyAllWindows()

