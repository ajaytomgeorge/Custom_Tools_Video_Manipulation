import cv2
import random 
import numpy as np

def Rand(start, end, num): 
    res = [] 
  
    for j in range(num): 
        res.append(random.randint(start, end)) 
  
    return res 


def subimage(image, center, theta, width, height):

   ''' 
   Rotates OpenCV image around center with angle theta (in deg)
   then crops the image according to width and height.
   '''
   originalimage=image

   # Uncomment for theta in radians
   #theta *= 180/np.pi

   shape = ( image.shape[1], image.shape[0] ) # cv2.warpAffine expects shape in (length, height)

   matrix = cv2.getRotationMatrix2D( center=center, angle=theta, scale=1 )
   image = cv2.warpAffine( src=image, M=matrix, dsize=shape )
   cv2.imshow("frame",image)
   cv2.waitKey(0)

   


   x = int( center[0] - width/2  )
   y = int( center[1] - height/2 )

   image = image[ y:y+height, x:x+width ]
   cv2.imshow("frame",image)
   cv2.waitKey(0)
   for i in range(20):
       x_offset=50+random.randint(100,300)
       y_offset=50+i*2
       originalimage[y_offset:y_offset+image.shape[0], x_offset:x_offset+image.shape[1]] = image

   return originalimage


image = cv2.imread('c1-100.jpg')
image = subimage(image, center=(110, 125), theta=5, width=50, height=50)
#image = subimage(image, center=(110, 125), theta=30, width=100, height=200)
cv2.imwrite('patch.jpg', image)