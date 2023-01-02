# Face-Detection

Human face detection project makes use of a video camera to input a scene and processes the scene to detect human faces. It uses two cascade classifiers, haarcascade_frontal_face_default.xml for face detection and haarcascade_eye_tree_eyeglasses.xml for the detection of eyes on the detected face. 
The project consists of two python scripts and two pretrained cascade classifiers XML files all in the same directory.
It makes use of three imports, viz. OpenCV, NumPy, and the above module extra.py. 
Firstly, both the cascade classifiers are loaded in, then the while loop to capture the video begins. Inside each iteration of the loop, the captured frame is converted to grayscale then bilateral filter is applied to reduce noises. Then the face is detected using the face cascade classifier and a circle is drawn over the area detected. The region of interest of face is also cropped and eye cascade classifier is applied to it for detecting eyes. A rectangle is drawn over each detected eye. 
