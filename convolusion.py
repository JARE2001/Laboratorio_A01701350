
import numpy as np
import matplotlib.pyplot as plt
import random
#import cv2

 


def total_conv(imagen,filtro):
    
    x=len(imagen[0])- len(filtro)+1
    y=len(imagen)- len(filtro)+1
    res = np.zeros((x,y))

    for i in range(x):
        for j in range(y):
            print(imagen[j:j+len(filtro[0]),i:i+len(filtro)])
            res[i][j] = np.sum(filtro * imagen[j:j+len(filtro[0]),i:i+len(filtro)])
    plt.imshow(res, cmap='gray')
    plt.show()

    return res


imagen = np.array( [[1, 2, 3, 4, 5, 6],
                    [7, 8, 9, 10, 11, 12],
                    [0, 0, 1, 16, 17, 18],
                    [0, 1, 0, 7, 23, 24],
                    [1, 7, 6, 5, 4, 3] ])

filtro = np.random.randint(10,size =(3,3))

print(total_conv(imagen,filtro))