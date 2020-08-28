import numpy as np

def RGB_TO_LAB(img):

    height, width, channel = img.shape

    def func(t):
        if (t > 0.008856):
            return np.power(t, 1/3.0);
        else:
            return 7.787 * t + 16 / 116.0;

    #Conversion Matrix
    matrix = [[0.412453, 0.357580, 0.180423],
            [0.212671, 0.715160, 0.072169],
            [0.019334, 0.119193, 0.950227]]

    _b = img[:, :, 0] 
    _g = img[:, :, 1] 
    _r = img[:, :, 2]

    lab_img = np.empty_like(img)

    for i in np.arange(height):
        for j in np.arange(width):
            r_ = _r[i, j] / 255
            g_ = _g[i, j] / 255
            b_ = _b[i, j] / 255

            # RGB values lie between 0 to 1.0
            rgb = [r_, g_, b_]

            cie = np.dot(matrix, rgb);

            cie[0] = cie[0] / 0.950456;
            cie[2] = cie[2] / 1.088754; 

            # Calculate the L
            L = 116 * np.power(cie[1], 1/3.0) - 16.0 if cie[1] > 0.008856 else 903.3 * cie[1];

            # Calculate the a 
            a = 500*(func(cie[0]) - func(cie[1]));

            # Calculate the b
            b = 200*(func(cie[1]) - func(cie[2]));

            #  Values lie between -128 < b <= 127, -128 < a <= 127, 0 <= L <= 100 
            Lab = [b , a, L]; 

            # OpenCV Format
            lab_img[i, j, 0] = L * 255 / 100;
            lab_img[i, j, 1] = a + 128;
            lab_img[i, j, 2] = b + 128;

            # Lab_OpenCV = [b , a, L]; 

    return lab_img

    