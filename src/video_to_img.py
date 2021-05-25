# Importing all necessary libraries
import cv2
import os

# Read the video from specified path
cam = cv2.VideoCapture("../Data/Video.mp4 ")

# frame
currentframe = 0

while(True):
	
	# reading from frame
	ret,frame = cam.read()
    print("yes")
	if ret:
        
		# if video is still left continue creating images
		name = '../Data/Images/cap_' + str(currentframe) + '.jpg'
		print ('Creating...' + name)

		# writing the extracted images
		cv2.imwrite(name, frame)

		# increasing counter so that it will
		# show how many frames are created
		currentframe += 1
        
	else:
		break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
