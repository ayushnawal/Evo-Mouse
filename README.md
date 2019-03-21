# Evo/Imaginary-Mouse

[![platform](https://img.shields.io/badge/Implementation-Python-blue.svg)](https://www.android.com)

Controls the mouse action through gestures using Image processing i.e. WebCam only. This tool 
will convert webcam to an imaginary mouse (hence the name). It is a cheap alternative to existing gesture control devices like evo. This project implements correlation-based tracking approach. Move the mouse by tracking a object. By the use of opencv library in Python (Image processing) , your palm will be detected and the mouse cursor will move according to the position of hand.

##Libraries used

opencv<br>
numpy<br>
common<br>
video<br>
win32api, win32con<br>
pyautogui<br>
sys, getopt

## Algorithm outline

![](https://i.imgur.com/AlmKvJ5.png))

1) Firstly, detecting the mean value of the selected area by converting frame received by Webcam to a Threshold using Grayscale for precision and Gaussian Blur for removing the noise.
2) After that, setting the position of the cursor accordingly as the position of hand.
3) For other events to happen, detection of the tips of the fingers through Edge detection technique.
4) Processing the number of dots (sticking two fingers together will give a single point only)
5) Using this technique and the area of palm, some other gesture features are implemented as mentioned below.

## Instruction to operate

1) See the count on the top left corner and set a value(count_max).
   When
     count = count_max-1 : LEFT Click
     count = count_max+1 : RIGHT Click
2) Just Place your Hand at the circle shown and press s to start.
3) Keys:
     SPACE    - pause video
     c        - clear targets
     s        - start using as a mouse and set the count
     esc      - close the program
4) Additional features:
     Double Click - By two consecutive left clicks
     Drag - Left Click, hold and Release
     Scroll Down - Reduce hand area and cursor position to lower half of screen  
     Scroll Up - Reduce hand area and cursor position to upper half of screen
     
## Acknowledgements
[Anmol Bansal](https://github.com/Anmolbansal1)
(Team Member)<br>
[Pranav Mistry’s  Mouseless](http://www.pranavmistry.com/projects/mouseless/)<br>(Reference)

Performance needs to be more optimized. Help us in improving through contributions/suggestions.