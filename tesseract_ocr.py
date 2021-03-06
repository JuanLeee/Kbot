import cv2
import pytesseract
import os
import numpy as np
import re
from pytessy.pytessy import PyTessy
import logging
import string, re
import sys
import unittest




class OCR_PyTes:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = self.resource_path('./Tesseract-OCR/tesseract.exe')
        self.ocr = PyTessy(self.resource_path('./Tesseract-OCR/tesseract.exe'))
        logging.info("setting up OCR")
        self.wtop = 179
        self.htop = 46
        self.wbot = 193
        self.hbot = 52
        
        # self.custom_config = r'--psm 13 --oem 3 outputbase digits'
        # self.custom_config = r'--oem 3 --psm 7'

    def resource_path(self,relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.dirname(__file__)
        return os.path.join(base_path, relative_path)

    def get_grayscale(self,image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # noise removal
    def remove_noise(image):
        return cv2.medianBlur(image,5)
    
    #thresholding
    def thresholding(self,image):
        return cv2.threshold(image,115,255,cv2.THRESH_BINARY)[1]

    #dilation
    def dilate(image):
        kernel = np.ones((5,5),np.uint8)
        return cv2.dilate(image, kernel, iterations = 1)
        
    #erosion
    def erode(image):
        kernel = np.ones((5,5),np.uint8)
        return cv2.erode(image, None, iterations = 2)

    #opening - erosion followed by dilation
    def opening(image):
        kernel = np.ones((5,5),np.uint8)
        return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    #canny edge detection
    def canny(image):
        return cv2.Canny(image, 100, 200)

    def invert(image):
        return cv2.bitwise_not(image) 

    #skew correction
    def deskew(image):
        coords = np.column_stack(np.where(image > 0))
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return rotated

    #template matching
    def match_template(image, template):
        return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

    def pytess_to_string(self,img):
        h, w = img.shape
        img_bytes = img.tobytes()
        bytesPerPixel = int(len(img_bytes) / (w * h))
        temp_string = self.ocr.read(img_bytes, w, h, bytesPerPixel)
        if temp_string is None:
            temp_string = ""
        p_string = re.sub('\n',' ',temp_string.lower())
        return re.sub(r'\s\s+' , ' ',re.sub('[^0123456789abcdefghijklmnopqrstuvwxyz QWERTYUIOPLKJHGFDSAZXCVBNM\']','', p_string)).strip()
    
    def pytess_to_string_nums(self,img):
        h, w = img.shape
        img_bytes = img.tobytes()
        bytesPerPixel = int(len(img_bytes) / (w * h))
        temp_string = self.ocr.read(img_bytes, w, h, bytesPerPixel)
        if temp_string is None:
            temp_string = "9999"
        p_string = re.sub('\n',' ',temp_string.strip().lower())
        num = 1
                
        length = len(p_string.split('-')[0])
        while length > 0:
            num *= 10
            length -= 1
        return int(num)
    
    def get_print_num(self,image,pos):
        try: 
            edition = self.get_edition_number(image,pos)
            if edition == 1:
                if pos == 0:
                    return self.pytess_to_string_nums(image[370:382,161:210])
                if pos == 1:
                    return self.pytess_to_string_nums(image[370:382,435:484])
                if pos == 2:
                    return self.pytess_to_string_nums(image[370:382,709:758])
                if pos == 3:
                    return self.pytess_to_string_nums(image[370:382,981:1030])
            elif edition == 2:
                if pos == 0:
                    return self.pytess_to_string_nums(image[372:385,163:217])
                if pos == 1:
                    return self.pytess_to_string_nums(image[372:385,437:491])
                if pos == 2:
                    return self.pytess_to_string_nums(image[372:385,711:765])
                if pos == 3:
                    return self.pytess_to_string_nums(image[372:385,985:1039])
            else:
                if pos == 0:
                    return self.pytess_to_string_nums(image[371:383,154:210])
                if pos == 1:
                    return self.pytess_to_string_nums(image[371:383,428:484])
                if pos == 2:
                    return self.pytess_to_string_nums(image[371:383,702:758])
                if pos == 3:
                    return self.pytess_to_string_nums(image[371:383,978:1032])
            return 9999
        except:
            return 9999
        
    def get_edition_number(self,image,pos):
        if pos == 0:
            red = (image[36,34][2])
        elif pos == 1:
            red = (image[36,308][2])
        elif pos == 2:
            red = (image[36,582][2])
        elif pos == 3:
            red = (image[36,856][2])
        if red > 170:
            return 1
        elif red < 80:
            return 2
        else:
            return 3

    def get_names_single(self,image,pos):
        try: 
            edition = self.get_edition_number(image,pos)
            if edition == 1:
                if pos == 0:
                    return self.pytess_to_string(image[57:103,47:226])
                if pos == 1:
                    return self.pytess_to_string(image[57:103,321:500])
                if pos == 2:
                    return self.pytess_to_string(image[57:103,594:773])
                if pos == 3:
                    return self.pytess_to_string(image[57:103,867:1046])
            elif edition == 2:
                if pos == 0:
                    return self.pytess_to_string(image[57:103,47:226])
                if pos == 1:
                    return self.pytess_to_string(image[57:103,321:500])
                if pos == 2:
                    return self.pytess_to_string(image[57:103,594:773])
                if pos == 3:
                    return self.pytess_to_string(image[57:103,867:1046])
            else:
                if pos == 0:
                    return self.pytess_to_string(image[58:103,52:226])
                if pos == 1:
                    return self.pytess_to_string(image[58:103,326:500])
                if pos == 2:
                    return self.pytess_to_string(image[58:103,599:773])
                if pos == 3:
                    return self.pytess_to_string(image[58:103,870:1046])
            return "-1"
        except:
            return "-1"

    def get_names_bottom(self,image,pos):
        try: 
            edition = self.get_edition_number(image,pos)
            if edition == 1:
                if pos == 0:
                    return self.pytess_to_string(image[310:362,47:238])
                if pos == 1:
                    return self.pytess_to_string(image[310:362,321:512])
                if pos == 2:
                    return self.pytess_to_string(image[310:362,594:785])
                if pos == 3:
                    return self.pytess_to_string(image[310:362,867:1058])
            elif edition == 2:
                if pos == 0:
                    return self.pytess_to_string(image[310:362,47:240])
                if pos == 1:
                    return self.pytess_to_string(image[310:362,321:514])
                if pos == 2:
                    return self.pytess_to_string(image[310:362,594:787])
                if pos == 3:
                    return self.pytess_to_string(image[310:362,867:1060])
            else:
                if pos == 0:
                    return self.pytess_to_string(image[314:362,60:234])
                if pos == 1:
                    return self.pytess_to_string(image[314:362,334:508])
                if pos == 2:
                    return self.pytess_to_string(image[314:362,607:781])
                if pos == 3:
                    return self.pytess_to_string(image[314:362,880:1054])
            return "-1"
        except:
            return "-1"
    
    def depose(self):
        del self.ocr
    

# ocr = OCR_PyTes()

# absolute_path = os.path.join(os.getcwd(), 'card (81).png')
# images = cv2.imread(absolute_path)

# print(ocr.get_names_single(images,0))
# print(ocr.get_names_single(images,1))
# print(ocr.get_names_single(images,2))
# print(ocr.get_names_single(images,3))

# print(ocr.get_names_bottom(images,0))
# print(ocr.get_names_bottom(images,1))
# print(ocr.get_names_bottom(images,2))
# print(ocr.get_names_bottom(images,3))

# # # # # print(ocr.get_print_num(images,3))

# absolute_path = os.path.join(os.getcwd(), 'card (83).png')
# images = cv2.imread(absolute_path)

# print(ocr.get_print_num(images,0))
# print(ocr.get_print_num(images,1))
# print(ocr.get_print_num(images,2))

