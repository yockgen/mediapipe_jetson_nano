import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("./test01.mp4")
with mp_face_detection.FaceDetection(
    min_detection_confidence=0.7) as face_detection:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = face_detection.process(image)

    # Draw the face detection annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.detections:
      for detection in results.detections:
        #mp_drawing.draw_detection(image, detection)
        nose = mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.NOSE_TIP)
        ih,iw,ic = image.shape
        x,y = int(nose.x*iw), int(nose.y*ih)
        cv2.putText(image,"NOSE", (x,y),cv2.FONT_HERSHEY_PLAIN, 1,(255,0,0),2)
    
    cv2.imshow('MediaPipe Face Detection', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break


cap.release()
