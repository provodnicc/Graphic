from re import L
import cv2
import numpy as np

def test_rgb2lab(new):
    for i in range(1, len(new)):
        for j in range(1, len(new[1])):
            var_R = ( new[i][j][0] / 255 )
            var_G = ( new[i][j][1] / 255 )
            var_B = ( new[i][j][2] / 255 )

            if ( var_R > 0.04045 ):
                var_R = ( ( var_R + 0.055 ) / 1.055 ) ** 2.4
            else:                   
                var_R = var_R / 12.92
            if( var_G > 0.04045 ):
                var_G = ( ( var_G + 0.055 ) / 1.055 ) ** 2.4
            else:
                var_G = var_G / 12.92
            if ( var_B > 0.04045 ): 
                var_B = ( ( var_B + 0.055 ) / 1.055 ) ** 2.4
            else:
                var_B = var_B / 12.92

            var_R = var_R * 100
            var_G = var_G * 100
            var_B = var_B * 100

            x = var_R * 0.4124 + var_G * 0.3576 + var_B * 0.1805
            y = var_R * 0.2126 + var_G * 0.7152 + var_B * 0.0722
            z = var_R * 0.0193 + var_G * 0.1192 + var_B * 0.9505

            var_X = x 
            var_Y = y 
            var_Z = z

            if ( var_X > 0.008856 ):
                 var_X = var_X** ( 1/3 )
            else:
                 var_X = ( 7.787 * var_X ) + ( 16 / 116 )
            if ( var_Y > 0.008856 ):
                 var_Y = var_Y ** ( 1/3 )
            else:
                 var_Y = ( 7.787 * var_Y ) + ( 16 / 116 )
            if ( var_Z > 0.008856 ):
                 var_Z = var_Z ** ( 1/3 )
            else:
                 var_Z = ( 7.787 * var_Z ) + ( 16 / 116 )

            l = (( 116 * var_Y ) - 16)
            a = 500 * ( var_X - var_Y )
            b = 200 * ( var_Y - var_Z )
            new[i][j][0] = l
            new[i][j][1] = a
            new[i][j][2] = b
    return(new)

def test_lab2rgb(new):
    for i in range(1, len(new)):
        for j in range(1, len(new[1])):
            l = new[i][j][0]
            a = new[i][j][1]
            b = new[i][j][2]
            var_Y = ( l + 16 ) / 116
            var_X = a / 500 + var_Y
            var_Z = var_Y - b / 200

            if ( var_Y**3  > 0.008856 ):
                 var_Y = var_Y**3
            else:
                 var_Y = ( var_Y - 16 / 116 ) / 7.787
            if ( var_X**3  > 0.008856 ):
                 var_X = var_X**3
            else:
                 var_X = ( var_X - 16 / 116 ) / 7.787
            if ( var_Z**3  > 0.008856 ):
                 var_Z = var_Z**3
            else:
                 var_Z = ( var_Z - 16 / 116 ) / 7.787

            x = var_X 
            y = var_Y
            z = var_Z

            var_X = x / 100
            var_Y = y / 100
            var_Z = z / 100

            var_R = var_X *  3.2406 + var_Y * -1.5372 + var_Z * -0.4986
            var_G = var_X * -0.9689 + var_Y *  1.8758 + var_Z *  0.0415
            var_B = var_X *  0.0557 + var_Y * -0.2040 + var_Z *  1.0570

            if ( var_R > 0.0031308 ):
                var_R = 1.055 * ( var_R ** ( 1 / 2.4 ) ) - 0.055
            else:
                var_R = 12.92 * var_R
            if ( var_G > 0.0031308 ):
                var_G = 1.055 * ( var_G ** ( 1 / 2.4 ) ) - 0.055
            else:
                var_G = 12.92 * var_G
            if ( var_B > 0.0031308 ):
                var_B = 1.055 * ( var_B ** ( 1 / 2.4 ) ) - 0.055
            else:
                var_B = 12.92 * var_B

            new[i][j][0] = var_R * 255
            new[i][j][1] = var_G * 255
            new[i][j][2] = var_B * 255
    return (new)

def rgb2lab(new):
    l = 0
    m = 0
    s = 0
    l_1 = 0
    a_1 = 0
    b_1 = 0
    labmass = np.zeros((len(new), len(new[1]), 3), dtype = 'float')
    for i in range(1, len(new)):
        for j in range(1, len(new[1])):
            r = new[i][j][2]
            g = new[i][j][1]
            b = new[i][j][0]
            
            # r = r*0.92157
            # g = g*0.92157
            # b = b*0.92157

            if (r < 3):
                r = 3
            if (g < 3):
                g = 3
            if (b < 3):
                b = 3
            # r = r/255
            # g = g/255
            # b = b/255

            l = np.log10(r*0.3811 + g*0.5783 + b*0.0402)
            m = np.log10(r*0.1967 + g*0.7244 + b*0.0782)
            s = np.log10(r*0.0241 + g*0.1288 + b*0.8444)

            l_1 = l*0.5774 + m*0.5774 + s*0.5774
            a_1 = l*0.4082 + m*0.4082 - s*0.8164
            b_1 = l*0.7071 - m*0.7071 + s*0

            labmass[i][j][0] = l_1
            labmass[i][j][1] = a_1
            labmass[i][j][2] = b_1
            # print(labmass[i][j])

    return(labmass)

def lab2rgb(new):
    l = 0
    m = 0
    s = 0
    l_1 = 0
    a_1 = 0
    b_1 = 0
    labmass = np.zeros((len(new), len(new[1]), 3), dtype = 'uint8')
    for i in range(1, len(new)):
        for j in range(1, len(new[1])):
            l_1 = new[i][j][0]
            a_1 = new[i][j][1]
            b_1 = new[i][j][2]
            l = 10**(l_1*0.5774 + a_1*0.5774 + b_1*0.5774)
            m = 10**(l_1*0.4082 + a_1*0.4082 - b_1*0.4082)
            s = 10**(l_1*0.7071 - a_1*0.7071*2 + b_1*0)
            temp   = 255*(l*4.4679 - m*3.5873 + s*0.1193)/0.92157
            temp_2 = 255*(-l*1.2186 + m*2.3809 - s*0.1624)/0.92157
            temp_3 = 255*(l*0.0497 - m*0.2439 + s*1.2045)/0.92157
            labmass[i][j][2] =  int(abs(temp))
            labmass[i][j][1] =  int(temp_2)
            labmass[i][j][0] =  int(temp_3)
    return(labmass)

def corr(orig,new):
    # перевод из rgb в lab

    # алгоритм
    sumrgb_orig = (0, 0, 0)
    sumrgb_new = (0, 0, 0)

    for i in range(1, len(orig)):
        for j in range(1, len(orig[1])):
            sumrgb_orig += orig[i][j]

    for i in range(1, len(new)):
        for j in range(1, len(new[1])):
            sumrgb_new += new[i][j]

    ee_orig=sumrgb_orig/len(orig)/len(orig[1])
    ee_new=sumrgb_new/len(new)/len(new[1])
    
    sumtemp_orig=(0,0,0)
    sumtemp_new=(0,0,0)


    for i in range(1, len(orig)):
        for j in range(1, len(orig[1])):
            sumtemp_orig+=((orig[i][j]-ee_orig)**2)
    d_orig=np.sqrt(sumtemp_orig/len(orig)/len(orig[1]))

    for i in range(1, len(new)):
        for j in range(1, len(new[1])):
            sumtemp_new+=((new[i][j]-ee_new)**2)
    d_new=np.sqrt(sumtemp_new/len(new)/len(new[1]))
    
    for i in range(1, len(orig)):
        for j in range(1, len(orig[1])):
            r = orig[i][j][0]
            g = orig[i][j][1]
            b = orig[i][j][2]
            l = np.log10(r*0.3811 + g*0.5783 + b*0.0402)
            m = np.log10(r*0.1967 + g*0.7244 + b*0.0782)
            s = np.log10(r*0.0241 + g*0.1288 + b*0.8444)
            l_1 = l*0.5774 + m*0.5774 + s*0.5774
            a_1 = l*0.4082 + m*0.4082 - s*0.4082
            b_1 = l*0.7071 - m*0.7071 + s*0
            orig[i][j][0] = l_1
            orig[i][j][1] = a_1
            orig[i][j][2] = b_1
            
    # присваивание\
    # new = cv2.cvtColor(img2, cv2.COLOR_RGB2LAB)
    # orig = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
    for i in range(1, len(new)):
        for j in range(1, len(new[1])):
            temp=ee_orig+(sumrgb_new-ee_new)*d_orig/d_new
            new[i][j][0]+=temp[0]
            new[i][j][1]+=temp[1]
            new[i][j][2]+=temp[2]
    
    # перевод из lab в rgb
    # new = lab2rgb(new)
    # new = cv2.cvtColor(new, cv2.COLOR_LAB2RGB)
    cv2.imshow('ad', new)
    cv2.waitKey()


img = cv2.imread('B.jpg')
img2 = cv2.imread('Y.jpg')

# img2 = rgb2lab(img2)
# img2 = lab2rgb(img2)

img2 = test_rgb2lab(img2) 
# corr(img, img2)
img2 = test_lab2rgb(img2) 
# img2 = cv2.cvtColor(img2, cv2.COLOR_LAB2RGB)
cv2.imshow('ad', img2)
cv2.waitKey()
