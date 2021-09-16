from PIL import Image
    
import cv2
import numpy as np


def clean(pilimg):
    
    # Conversion from PIL image to array
    img = 255 - np.array(pilimg.convert('L'))
    
    # Resize with constant "long dimension" (consistent with 330 dpi on an 8.5"X11" page)
    L = 3300.00

    if img.shape[0] < img.shape[1]:
        scale = L/img.shape[1]
        height = int(img.shape[0] * scale)
        width = int(L)
        dim = (width, height)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    else:
        scale = L/img.shape[0] 
        width = int(img.shape[1] * scale)
        height = int(L)
        dim = (width, height)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    # Blur resized image
    blur = cv2.GaussianBlur(resized,(3,3),10)
    _,th = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    # Attempt to distinguish horizontal lines
    horz_ker = cv2.getStructuringElement(cv2.MORPH_RECT, (101,1))
    horz_img = cv2.erode(th, horz_ker, iterations=1)
    horz_img = cv2.dilate(horz_img, horz_ker, iterations=1)
    
    # Attempt to distinguish vertical lines
    vert_ker = cv2.getStructuringElement(cv2.MORPH_RECT, (1,101))
    vert_img = cv2.erode(th, vert_ker, iterations=1)
    vert_img = cv2.dilate(vert_img, vert_ker, iterations=1)
    
    close_ker = cv2.getStructuringElement(cv2.MORPH_RECT,(1,1))
    
    # Merge horizontal and vertical line "masks"
    mask = cv2.bitwise_or(horz_img,vert_img)
    mask = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,close_ker,iterations =1)
    
    # Detect long lines in mask and thicken
    lines = cv2.HoughLinesP(mask,
                            rho = 1,
                            theta = np.pi/2,
                            threshold = 150,
                            minLineLength=100,
                            maxLineGap=10)
    if lines is not None:
        for line in lines:
            for x1,y1,x2,y2 in line:
                pt1 = (x1,y1)
                pt2 = (x2,y2)
                cv2.line(mask, pt1, pt2, (255), 7)
      
    
    open_ker = cv2.getStructuringElement(cv2.MORPH_RECT,(1,1))

    # Clean Final image
    final = cv2.morphologyEx(cv2.bitwise_and(th.copy(),cv2.bitwise_not(mask.copy())),cv2.MORPH_OPEN,open_ker,iterations = 1)
    
      
    # Conversion to PIL image from array
    return Image.fromarray(255 - final) 



