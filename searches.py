import mysql.connector
import face_recognition
import cv2
from PIL import Image
import os



MyDB = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',
        database='trial',
        charset='utf8'
        )
MyCursor = MyDB.cursor()


MyCursor.execute("Select * from images where id = %uid ;")


def linear_search(arr, target):

    for index, element in enumerate(arr):

        if element == target:
            return index

    return -1

# Example usage
arr = [2, 5, 1, 9, 7, 3]
target = 10


result = linear_search(arr, target)


if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the list.")





def sentinel_linear_search(arr, target):

    arr.append(target)
    index = 0


    while arr[index] != target:
        index += 1


    arr.pop()


    if index < len(arr):
        return index
    else:
        return -1

# Example usage
arr = [2, 5, 1, 9, 7, 3, 6]
target = 2


result = sentinel_linear_search(arr, target)


if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the list.")





def binary_search(arr, low, high, x):


	if high >= low:

		mid = (high + low) // 2


		if arr[mid] == x:
			return mid


		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)


		else:
			return binary_search(arr, mid + 1, high, x)

	else:

		return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 4


result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
      


import math as mt
def bsearch(A, key_to_search):

	n = len(A)

	lg = int(mt.log2(n-1)) + 1;



	pos = 0
	for i in range(lg - 1, -1, -1) :
		if (A[pos] == key_to_search):
			return pos


		new_pos = pos | (1 << i)


		if ((new_pos < n) and
			(A[new_pos] <= key_to_search)):
			pos = new_pos


	return (pos if(A[pos] == key_to_search) else -1)


if __name__ == "__main__":

	A = [ -2, 10, 100, 250, 32315 ]
	print( bsearch(A, 100))#The result "-1" means the element is not found
	




import math as mt


def ternarySearch(l, r, key, ar):

	if (r >= l):


		mid1 = l + (r - l) //3
		mid2 = r - (r - l) //3


		if (ar[mid1] == key):
			return mid1

		if (ar[mid2] == key):
			return mid2


		if (key < ar[mid1]):


			return ternarySearch(l, mid1 - 1, key, ar)

		elif (key > ar[mid2]):


			return ternarySearch(mid2 + 1, r, key, ar)

		else:


			return ternarySearch(mid1 + 1,
								mid2 - 1, key, ar)


	return -1
#example


# Driver code
l, r, p = 0, 9, 5

# Get the array
# Sort the array if not sorted
ar = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# Starting index
l = 0

# end element index
r = 9

# Checking for 5

# Key to be searched in the array
key = 5

# Search the key using ternarySearch
p = ternarySearch(l, r, key, ar)

# Print the result
print("Index of", key, "is", p)

# Checking for 50

# Key to be searched in the array
key = 50

# Search the key using ternarySearch
p = ternarySearch(l, r, key, ar)

# Print the result
print("Index of", key, "is", p)



import math as mt

def jumpSearch( arr , x , n ):


	step = mt.sqrt(n)


	prev = 0
	while arr[int(min(step, n)-1)] < x:
		prev = step
		step += mt.sqrt(n)
		if prev >= n:
			return -1


	while arr[int(prev)] < x:
		prev += 1


		if prev == min(step, n):
			return -1


	if arr[int(prev)] == x:
		return prev

	return -1

#test function
arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
	34, 55, 89, 144, 233, 377, 610 ]
x = 21
n = len(arr)

# Find the index of 'x' using Jump Search
index = jumpSearch(arr, x, n)

# Print the index where 'x' is located
print("Number" , x, "is at index" ,"%.0f"%index)#The result "-1" means the element is not found




def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
      pos = low + ((target - arr[low]) * (high - low)) / (arr[high] - arr[low])
      if pos < low or pos > high:
        if target < arr[low]:
         high = low - 1
        else:
         low = low + 1
      else:
        if arr[int(pos)] == target:
          return int(pos)
        elif arr[int(pos)] < target:
          low = int(pos) + 1
        else:
          high = int(pos) - 1

    return -1

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 17

result = interpolation_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the list.")
	




def exponential_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1

    low = 0
    high = min(1, n - 1)

    while high < n and arr[high] < target:
        low = high + 1
        high = min(2 * high, n - 1)

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage
arr = [1, 2, 4, 9, 16, 25, 36, 49, 64, 81, 100]
target = 36

result = interpolation_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the list.")





from bisect import bisect_left




def fibMonaccianSearch(arr, x, n):


    fibMMm2 = 0
    fibMMm1 = 1
    fibM = fibMMm2 + fibMMm1


    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1


    offset = -1


    while (fibM > 1):


        i = min(offset+fibMMm2, n-1)


        if (arr[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i


        elif (arr[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1


        else:
            return i


    if(fibMMm1 and arr[n-1] == x):
        return n-1


    return -1


#Example
arr = [10, 22, 35, 40, 45, 50,
       80, 82, 85, 90, 100,235]
n = len(arr)
x = 100
ind = fibMonaccianSearch(arr, x, n)
if ind>=0:
  print("Found at index:",ind)
else:
  print(x,"isn't present in the array")


def encode_faces(self):
    for image in os.listdir('faces'):
        face_image = face_recognition.load_image_file(f'faces/{image}')
        face_encoding = face_recognition.face_encodings(face_image)[0]        
        self.known_face_encodings.append(face_encoding)
        self.knows_face_names.append(image)
    print(self.knows_face_names)


