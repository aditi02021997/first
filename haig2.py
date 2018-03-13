Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy
>>> import cv2

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import cv2
ImportError: DLL load failed: %1 is not a valid Win32 application.

>>> import cv2

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import cv2
ImportError: DLL load failed: %1 is not a valid Win32 application.
>>> import cv2
>>> print cv2.__version__
3.4.1

>>> import numpy as np
>>> import cv2
>>> img = imread('father.jpg',0)

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    img = imread('father.jpg',0)
NameError: name 'imread' is not defined
>>> img = imread('father.jpg',0)

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    img = imread('father.jpg',0)
NameError: name 'imread' is not defined
>>> img = cv2.imread('father.jpg',0)
>>> print img
[[161 160 165 ... 147 141 138]
 [160 160 161 ... 148 142 139]
 [160 161 160 ... 146 140 138]
 ...
 [193 194 194 ... 152 152 151]
 [192 194 198 ... 152 152 152]
 [191 193 197 ... 151 152 152]]
>>> cv2.imshow('father',img)
>>> cv2.imshow('father',img)
>>> 
=============================== RESTART: Shell ===============================
>>> img = cv2.imread('C:/Users/Desktop/father.jpg',0)

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    img = cv2.imread('C:/Users/Desktop/father.jpg',0)
NameError: name 'cv2' is not defined
>>> import numpy as np
>>> import cv2
>>> img = cv2.imread('C:/Users/Desktop/father.jpg',0)
>>> cv2.imshow('father',img)

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    cv2.imshow('father',img)
error: OpenCV(3.4.1) C:\build\master_winpack-bindings-win32-vc14-static\opencv\modules\highgui\src\window.cpp:356: error: (-215) size.width>0 && size.height>0 in function cv::imshow

>>> print img
None

>>> img = cv2.imread('C:/Users/Desktop/father.jpg',0)

>>> print img
None
>>> img = cv2.imread('C:/Users/ADITI SHARMA/Desktop/father.jpg',0)
>>> print img
[[161 160 165 ... 147 141 138]
 [160 160 161 ... 148 142 139]
 [160 161 160 ... 146 140 138]
 ...
 [193 194 194 ... 152 152 151]
 [192 194 198 ... 152 152 152]
 [191 193 197 ... 151 152 152]]

>>> cv2.imshow('father',img)
>>> cv2.imshow('father',img)
>>> cv2.waitKey(0)
-1
>>> 
