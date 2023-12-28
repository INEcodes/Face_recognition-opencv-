from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from time import strftime
from datetime import datetime
import numpy as np

def reg_faces(frame, faces):
    for (x, y, w, h) in faces:
        face_region = frame[y:y+h, x:x+w]
        blurred_face = cv2.GaussianBlur(face_region, (1, 1), 0)
        frame[y:y+h, x:x+w] = blurred_face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return frame

video_capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
detected_faces = []
while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    detected_faces = faces

    frame = reg_faces(frame, detected_faces)

    cv2.imshow("Recognize Faces", frame)

    if cv2.waitKey(1) != -1:
        break

video_capture.release()
cv2.destroyAllWindows()

