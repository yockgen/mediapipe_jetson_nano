#!/usr/bin/env python
# coding: utf-8

# In[8]:


import cv2
import mediapipe as mp

# In[9]:


cap = cv2.VideoCapture("./test01.mp4")
#cap = cv2.VideoCapture(0)

# In[10]:

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=10)

while True:
    success,img =cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
       for faceLms in results.multi_face_landmarks:
         mpDraw.draw_landmarks(img,faceLms,mpFaceMesh.FACE_CONNECTIONS) 
    img = cv2.resize(img, (960, 540))
    cv2.imshow("Image",img)
    cv2.waitKey(1)


# In[ ]:




