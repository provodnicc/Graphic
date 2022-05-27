import cv2
import numpy as np
import matplotlib.pyplot as plt

def gist(img):
    r = np.zeros((256))
    g = np.zeros((256))
    b = np.zeros((256))

    it = np.zeros((256))

    for i in range(1,len(img)):
        for j in range (1,len(img[1])):
            g[img[i][j][0]] += 1
            b[img[i][j][1]] += 1
            r[img[i][j][2]] += 1

    for i in range(0,256):
        it[i] = i
    plt.plot(it, r, color = 'r')
    plt.plot(it, b, color='b')
    plt.plot(it, g, color='g')
    plt.show()

img = cv2.imread('2.jpg')
gist(img)