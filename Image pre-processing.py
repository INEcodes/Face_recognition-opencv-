#Resizing 
from PIL import Image


image = Image.open("input_image.jpg")


new_width = 300
new_height = 200


resized_image = image.resize((new_width, new_height))


resized_image.save("output_image.jpg")


image.close()
resized_image.close()


#RGB to Grayscale

import cv2 


image = cv2.imread('C:\\Documents\\full_path\\tomatoes.jpg') 
cv2.imshow('Original', image) 
cv2.waitKey(0) 


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

cv2.imshow('Grayscale', gray_image) 
cv2.waitKey(0) 


cv2.destroyAllWindows()



#saving in database

import mysql.connector

MyDB = mysql.connector.connect{
	host='localhost',
	user='root',
	password='1234',
	database='trial',
	charset='utf8'}

MyCursor = MyDB.cursor()


MyCursor.execute("CREATE TABLE IF NOT EXISTS Images(id INTEGER(45) NOT NULL AUTO_INCREMENT PRIMARY KEY, Photo LONGBLOB NOT NULL")

def InsertBlob(FilePath):
	with open(FilePath, "rb") aa File:
		BinaryData = File.read()
	SQLStatement = "INSERT INTO Images(Photo) Values (%s)"
	MyCursor.execute(SQLStatement, (BinaryData, ))
	MyDB.commit()

def RetrieveBlob(ID):
	SQLStatement2 = "SELECT * FROM Images WHERE id = '{0}'"
	MyCursor.execute(SQLStatement2.format(str(ID)))
	MyResult = MyCursor.fetchone()[1]
	StoreFilePath = "ImageOutput/img{0}.jpg".format(str(ID))
	print(MyResult)
	with open(StoreFilePath, "wb") as File:
		File.write(MyResult)
		File.close()
