import cv2
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
mouth_cascade_path = 'haarcascade_mcs_mouth.xml'

if not os.path.exists(mouth_cascade_path):
    raise FileNotFoundError(f"{mouth_cascade_path} not found. Please download it and place it in the correct directory.")

mouth_cascade = cv2.CascadeClassifier(mouth_cascade_path)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        mouths = mouth_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=11, minSize=(30, 30))
        
        for (mx, my, mw, mh) in mouths:
            if my > h/2:
                cv2.rectangle(roi_color, (mx, my), (mx+mw, my+mh), (0, 255, 0), 2)
    
    cv2.imshow('Face and Mouth Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
