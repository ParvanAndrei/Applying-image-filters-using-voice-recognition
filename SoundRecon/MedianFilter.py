import sys
import cv2
import os
import numpy as np
import glob

DELAY_CAPTION = 1500
DELAY_BLUR = 100
MAX_KERNEL_LENGTH = 31

src = None
dst = None
window_name = 'Smoothing Demo'

def main():
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
    listFiles = glob.glob('images/*jpg')
    imageName =max(listFiles, key = os.path.getctime)
    #imageName = max(listFiles, key = os.path.getctime) if imageName = None else 'images/testimage1.jpg'
    global src
    src = cv2.imread(cv2.samples.findFile(imageName))
    if src is None:
        print ('Error opening image')
        print ('Usage: smoothing.py [image_name -- default ../data/lena.jpg] \n')
        return -1

    if display_caption('Original Image') != 0:
        return 0
    global dst
    dst = np.copy(src)
    if display_dst(DELAY_CAPTION) != 0:
        return 0

    if display_caption('Median Blur') != 0:
        return 0
    for i in range(1, MAX_KERNEL_LENGTH, 2):
        dst = cv2.medianBlur(src, i)
        if display_dst(DELAY_BLUR) != 0:
            return 0
#    display_caption('Done!')
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
    return 0


def loadImage(folder):
	images = []
	for filename in os.listdir(folder):
		img = cv2.imread(os.path.join(folder,filename))
		if img is not None:
			images.append(img)
	return images


#location = "images/"
#image = loadImage(location)
#image = cv2.imread('images/testimage1.jpg')
#imageResize = cv2.resize(image[1], (300,300))
#cv2.imshow('Imagetest', imageResize)
#cv2.waitKey(0)
#main(imageResize)


def display_caption(caption):
    global dst
    dst = np.zeros(src.shape, src.dtype)
    rows, cols, _ch = src.shape
    cv2.putText(dst, caption,
                (int(cols / 4), int(rows / 2)),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
    return display_dst(DELAY_CAPTION)
def display_dst(delay):
    cv2.imshow(window_name, dst)
    cv2.imwrite('images/dst_median.jpg', dst)
    c = cv2.waitKey(delay)
    if c >= 0 : return -1
    return 0
    


if __name__ == "__main__":
    filename = "images/ceva.jpg"
    main()
