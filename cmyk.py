
import cv2
import numpy as np

RGB_SCALE = 255
CMYK_SCALE = 100

def RGB_TO_CMYK(img):

    height, width, channel = img.shape

    B = img[:, :, 0].astype(float) 
    G = img[:, :, 1].astype(float) 
    R = img[:, :, 2].astype(float) 

    B_ = np.copy(B)
    G_ = np.copy(B)
    R_ = np.copy(B)

    K = np.zeros_like(B) 
    C = np.zeros_like(B) 
    M = np.zeros_like(B) 
    Y = np.zeros_like(B) 

    for i in np.arange(height):
        for j in np.arange(width):
            B_[i, j] = B[i, j] / RGB_SCALE
            G_[i, j] = G[i, j] / RGB_SCALE
            R_[i, j] = R[i, j] / RGB_SCALE
            
            K[i, j] = 1 - max(B_[i, j], G_[i, j], R_[i, j])

            if (B_[i, j], G_[i, j], R_[i, j]) == (0, 0, 0):
                C[i][j] = M[i][j] = Y[i][j] = 0
            else:
                C[i, j] = (1 - R_[i, j] - K[i, j])/(1 - K[i, j])
                M[i, j] = (1 - G_[i, j] - K[i, j])/(1 - K[i, j])
                Y[i, j] = (1 - B_[i, j] - K[i, j])/(1 - K[i, j])

    cmyk = np.dstack((C, M, Y, K))

    return cmyk

def RGB_TO_CMYK2(img):

    height, width, channel = img.shape

    B = img[:, :, 0]
    G = img[:, :, 1]
    R = img[:, :, 2]

    K = np.zeros_like(B) 
    C = np.zeros_like(B) 
    M = np.zeros_like(B) 
    Y = np.zeros_like(B) 

    for i in np.arange(height):
        for j in np.arange(width):

            if (R[i, j], G[i, j], B[i, j]) == (0, 0, 0):
                # black
                C[i, j] = 0
                M[i, j] = 0
                Y[i, j] = 0
                K[i, j] = CMYK_SCALE
            else: 
                # rgb [0,255] -> cmy [0,1]
                c = 1 - R[i, j] / RGB_SCALE
                m = 1 - G[i, j] / RGB_SCALE
                y = 1 - B[i, j] / RGB_SCALE

                # extract out k [0, 1]
                min_cmy = min(c, m, y)
                c = (c - min_cmy) / (1 - min_cmy)
                m = (m - min_cmy) / (1 - min_cmy)
                y = (y - min_cmy) / (1 - min_cmy)
                k = min_cmy

                C[i, j] = c * CMYK_SCALE
                M[i, j] = m * CMYK_SCALE
                Y[i, j] = y * CMYK_SCALE
                K[i, j] = k * CMYK_SCALE

    cmyk = np.dstack((C, M, Y, K))

    return cmyk