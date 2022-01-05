
# Importing all necessary libraries
import cv2
import os
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
  
# Read the video from specified path
cam = cv2.VideoCapture(filename)
  
try:
      
    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')
  
# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')
  
# frame
currentframe = 0

current_dir, video_name =  os.path.split(filename)
folder_name, ext = os.path.splitext(video_name)
if not os.path.exists(current_dir + '/' + folder_name):
    os.mkdir(current_dir + '/' + folder_name )

while(True):
      
    # reading from frame
    ret,frame = cam.read()
  
    if ret:
        # if video is still left continue creating images
        name = current_dir + '/' + folder_name + '/' + str(currentframe).zfill(8) + '.jpg'
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