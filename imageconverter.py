import glob
import cv2

ftypeI = input("input format jpg or png or other")
ftypeO = input("output format jpg or png or other")

for file in glob.glob("*." + ftypeI):
    img = cv2.imread(file)
    filename = file[:-4] + '.' + ftypeO
    print
    cv2.imwrite(filename, img) 


