
import numpy as np
import cv2
import matplotlib.pyplot as plt
 



def total_conv(imagen,filtro):
    res = np.zeros(imagen.shape)

    for i in range(len(imagen[0])):
        for j in range(len(imagen)):
            res[i][j] = np.sum(filtro * imagen[:len(filtro[0]),:len(filtro)])
    return res