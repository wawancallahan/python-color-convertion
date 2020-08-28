import numpy as np

def RGB_TO_XYZ(img):

    height, width, channel = img.shape

    _b = img[:, :, 0] 
    _g = img[:, :, 1] 
    _r = img[:, :, 2]

    xyz = np.empty_like(img)

    for i in np.arange(height):
        for j in np.arange(width):
            r_ = _r[i, j] / 255
            g_ = _g[i, j] / 255
            b_ = _b[i, j] / 255

            if ( r_ > 0.04045 ):
                r_ = ( ( r_ + 0.055 ) / 1.055 ) ** 2.4
            else:
                r_ = r_ / 12.92
            if ( g_ > 0.04045 ):
                g_ = ( ( g_ + 0.055 ) / 1.055 ) ** 2.4
            else:
                g_ = g_ / 12.92
            if ( b_ > 0.04045 ):
                b_ = ( ( b_ + 0.055 ) / 1.055 ) ** 2.4
            else:
                b_ = b_ / 12.92

            r_ = r_ * 100
            g_ = g_ * 100
            b_ = b_ * 100

            X = r_ * 0.4124564 + g_ * 0.3575761 + b_ * 0.1804375
            Y = r_ * 0.2126729 + g_ * 0.7151522 + b_ * 0.0721750
            Z = r_ * 0.0193339 + g_ * 0.1191920 + b_ * 0.9503041
            
            xyz[i, j, 0] = X
            xyz[i, j, 1] = Y
            xyz[i, j, 2] = Z

    return xyz