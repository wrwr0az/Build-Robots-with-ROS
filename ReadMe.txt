I useed open CV on Ubuntu 20.04 with using python3

First thing you should install all libraries 
Second you must check if casscade files are install (location.. /home/YourUserName/opencv/data/haarcascades/) you needs two files 
1- haarcascade_frontalface_alt.xml
2- haarcascade_eye_tree_eyeglasses.xml


but this folder in home directory 

now run the code from Terminal by write the follwing command

python3 DetectionFromCamera.py