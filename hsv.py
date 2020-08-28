import cv2
import numpy as np
import math

def RGB_TO_HSV(img):
    height, width, channel = img.shape

    B = img[:, :, 0].astype(float) 
    G = img[:, :, 1].astype(float) 
    R = img[:, :, 2].astype(float) 

    B_ = np.copy(B)
    G_ = np.copy(B)
    R_ = np.copy(B)

    H_ = np.zeros_like(B) 
    S_ = np.zeros_like(B) 
    V_ = np.zeros_like(B) 

    for i in np.arange(height):
        for j in np.arange(width):
            B_[i, j] = B[i, j] / 255
            G_[i, j] = G[i, j] / 255
            R_[i, j] = R[i, j] / 255

            Cmax = max(R_[i, j], G_[i, j], B_[i, j])
            Cmin = min(R_[i, j], G_[i, j], B_[i, j])
            delta = Cmax-Cmin

            # Hue Calculation
            if delta == 0:
                H = 0
            elif Cmax == R_[i, j]:
                H = (60 * ((G_[i, j] - B_[i, j]) / delta) + 360) % 360
            elif Cmax == G_[i, j]:
                H = (60 * ((B_[i, j] - R_[i, j]) / delta) + 120) % 360
            elif Cmax == B_[i, j]:
                H = (60 * ((R_[i, j] - G_[i, j]) / delta) + 240) % 360

            # Saturation Calculation
            if Cmax == 0:
                S = 0
            else :
                S = delta / Cmax
            
            # Value Calculation
            V = Cmax 

            H_[i][j] = H
            S_[i][j] = S
            V_[i][j] = V

    hsv = np.dstack((H_, S_, V_))

    return hsv