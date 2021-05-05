

def celda_conv(subMatriz, filtro):
    res = 0
    for i in range( len(filtro)):
        for j in range( len(filtro)):
             result += subMatriz[row][col] *  filtro[row][col]
    return res  

def total_conv(imagen,filtro):
    
    res = np.zeros(imagen.shape)

    for i in range(len(imagen[0])):
        for j in range(len(imagen)):
            res[i][j] = = np.sum(filtro * imagen[:len(filtro[0]), :len(filtro])

    