import cv2
import numpy as np
import random
#Start of code by ChatGBT

img1 = cv2.imread('cuarto1.PNG')
img2 = cv2.imread('cuarto2.PNG')


img1 = cv2.resize(img1, (300, 300))
img2 = cv2.resize(img2, (300, 300))


gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


mse = np.mean((gray1 - gray2) ** 2)


similarity = (1 - mse) * 100


print("Similarity:", similarity)

#End of code by ChatGBT
if similarity >50 :
    random_number=random.randint(1,100)
    print(random_number)
else:
    print("Clean your room")



