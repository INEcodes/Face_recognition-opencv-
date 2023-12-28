import numpy
import numpy.typing as npt
import os
from os import listdir
from typing import cast, Type, Sequence
import typing
import mysql.connector
#from flask import Flask, request, send_file
'''
RGB: typing.TypeAlias = 'numpy.dtype[numpy.uint8]'
ThreeD: typing.TypeAlias = tuple[int, int, int]
NDArrayRGB: typing.TypeAlias = 'numpy.ndarray[ThreeD, RGB]'
'''
#def load_images(paths: list[str]) -> tuple[list[NDArrayRGB], list[str]]: ...
#Resizing
from PIL import Image
import cv2
#from cv2 import cv2_imshow


def resize(im,new_width):
    width,height = im.size
    ratio = height/width
    new_height = int(ratio*new_width)
    resized_image = im.resize((new_width,new_height))
    return resized_image

def Grayscale(im,filepath):
    image = cv2.imread(filepath)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return gray

def upload_image(im,filepath):
    
    BinaryData = filepath
    SQLStatement = "INSERT INTO Images(Photo) Values (%s)"
    MyCursor.execute(SQLStatement, (BinaryData,))
    MyDB.commit()
    return "Image uploaded successfully"
                
                    
            
    

folder_dir = "D:/Coding/2nd year project(face recognition)/Dataset/dataset/images/train"

 
files = os.listdir(folder_dir)
extension = ['jpg','jpeg','png','gif']
for file in files:
    ext = file.split(".")[-1]
    if ext in extension:
        filepath = f"D:/Coding/2nd year project(face recognition)/Dataset/dataset/images/train/{file}"
        im = Image.open(filepath)
        im = resize(im,100)
        im = Grayscale(im,filepath)
        im = Image.open(filepath)
        
        

        MyDB = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',
        database='trial',
        charset='utf8'
        )

        MyCursor = MyDB.cursor()


        MyCursor.execute("CREATE TABLE IF NOT EXISTS Images(id INTEGER(45) NOT NULL AUTO_INCREMENT PRIMARY KEY, Photo LONGBLOB NOT NULL)")

        upload_image(im,filepath)
        im = Image.open(filepath)



        
        

        
        
        
