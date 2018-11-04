import numpy as np
import cv2
from matplotlib import pyplot as plt

im = cv2.imread('/home/suayder/Desktop/Fotos_Buracos/800X600/positives/DJI_0055.JPG', 0)

#cv2.imshow('aaa', im)

im = im[:450,200:700]
arr = im[214:215,0:500]
im = cv2.rectangle(im, (0,210),(500,220),(0,0,0),2)

arr = cv2.resize(arr, (500,30))
cv2.imshow('sad', arr)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('line.jpg',arr)
arr = arr.reshape((500,))
xaxys = np.arange(500)
#plt.step(xaxys, arr)
#plt.ylabel('grandeza em cinza', size=18)
#plt.savefig('imagefunc.pdf')
#plt.show()