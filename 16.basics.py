import numpy as np
import cv2
b = np.zeros([320,320],dtype = 'uint8')
n=40
j=n
while(j<=320):
    i=n
    while(i<=320):
             b[j-n:j,i-n:i] = 255
             b[j:j+n,i:i+n] = 255
             i=i+n*2
    j=j+n*2
cv2.imshow('Checker board 8*8',b)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
