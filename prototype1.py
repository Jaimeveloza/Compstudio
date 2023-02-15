import cv2
import numpy as np
import glob
import random
#Start of code from Pysource :https://pysource.com/2018/07/27/check-if-a-set-of-images-match-the-original-one-with-opencv-and-python/
original = cv2.imread("cuarto2.PNG")
duplicate = cv2.imread("cuarto2.PNG")

 

image1 = original.shape
image2 = duplicate.shape

if original.shape == duplicate.shape:
    print("The images have the same size and channels")
    difference = cv2.subtract(original, duplicate)
    b,g,r = cv2.split (difference)
    cv2.imshow("b",b)
    cv2.imshow("g",g)
    cv2.imshow("g",g)

    cv2.imshow("Difference", difference)
    print(cv2.countNonZero(b))
    print(cv2.countNonZero(g))
    print(cv2.countNonZero(r))
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r)==0:
        print("The images are completely equal") 
        #added random number generator 
        random_number = random.randint(1, 100)
        print(random_number)

        
        
    else:
        print("The Images aren't Equal")
else:
    print("Images are not the same size")


print(image1)
print(image2)

cv2.imshow("Original", original)
cv2.imshow("Duplicate", duplicate)
cv2.waitKey(0)
cv2.destroyAllWindows()

#end of code frtom pysource
