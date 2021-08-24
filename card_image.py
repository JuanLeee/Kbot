import urllib
import cv2 as cv
import numpy as np
import sys
import os
import argparse
import time
import urllib 
import requests
import timeit
from contextlib import closing
import gc


wtop = 179
htop = 46
wbot = 193
hbot = 52


class MyImage:
    def __init__(self, img_name, image):
        self.img = image
        self.name = img_name

    def __str__(self):
        return self.name

def run_fast_scandir(dir, ext):    
    subfolders, files = [], []

    for f in os.scandir(dir):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
            if os.path.splitext(f.name)[1].lower() in ext:
                files.append(f.path)
                print(f.path)


    for dir in list(subfolders):
        sf, f = run_fast_scandir(dir, ext)
        subfolders.extend(sf)
        files.extend(f)
    return files

def image_prune(img, filename):
    if img is not None:
        print('Pruned')
        if filename[1] == '3':
            if filename[0] == '1':
                 img = img[35:45,30:100]
            elif filename[0] == '2':
                img = img[35:45,161:231]
            elif filename[0] == '3':
                img = img[35:45,292:362]
            else:
                print('Wrong file name')
        elif filename[1] == '4':
            if filename[0] == '1':
                img = img[25:35,15:85]
            elif filename[0] == '2':
                img = img[25:35,151:185]
            elif filename[0] == '3':
                img = img[25:35,215:285]
            elif filename[0] == '4':
                img = img[25:35,315:385]
            else:
                print('Wrong file name')
        else:
            print('Wrong file name')
    else:
        print('Not pruned')
    return img



def load_images_from_folder(folder):
    folder = absolute_path = os.path.join(os.getcwd(), 'Kbot' , folder)
    images = []
    for filename in os.listdir(folder):
        sub_dir_path = folder + '/' + filename
        if (os.path.isdir(sub_dir_path)):
            for image_name in os.listdir(sub_dir_path):
                img = cv.imread(os.path.join(sub_dir_path,image_name))
                print(image_name)
                img = image_prune(img,image_name)
                images.append(MyImage(image_name,img))
        else: 
            img = cv.imread(os.path.join(folder,filename))
            print(filename)
            img = image_prune(img,filename)
            images.append(MyImage(filename,img))
    print(len(images))
    return images

def dhash(image, x = 70,y = 10):
    # convert the image to greyscale
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
	# resize the input image, adding a single column (width) so we
	# can compute the horizontal gradient
    resized = cv.resize(image, (x + 1, y))
	# compute the (relative) horizontal gradient between adjacent
	# column pixels
    diff = resized[:, 1:] > resized[:, :-1]
	# convert the difference image to a hash
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

def hash_table_create(folder):
    hash_table_images = {}
    images = load_images_from_folder(folder)
    for i in images:
        image_hash = dhash(i.img)
        hash_table_images[image_hash] = int(i.name[0])
    return hash_table_images


def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
    resp = None
    page = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    with closing(urllib.request.urlopen(page)) as resp:
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv.imdecode(image, cv.IMREAD_COLOR)
        gc.collect()
        return image
	# return the image


def get_position_hash(url,hash_table):
    images = []
    img = url_to_image(url)
    if url[-1] == '8':
        if dhash(img[35:45,30:100]) in hash_table:
            return 1
        if dhash(img[35:45,161:231]) in hash_table:
            return 2
        if dhash(img[35:45,292:362]) in hash_table:
            return 3
    elif url[-1] == '9':
        if dhash(img[22:37,17:79]) in hash_table:
            return 1
        if dhash(img[22:37,116:180]) in hash_table:
            return 2
        if dhash(img[22:37,215:277]) in hash_table:
            return 3
        if dhash(img[25:35,351:385]) in hash_table:
            return 4
    return -1

# def get_names(url,dimensions):
#     strings = []
#     img = url_to_image(url)
#     h, w, c = img.shape
#     if w < 900:
#         strings.append(pytess_to_string(img[57:103,47:226],w3,h3))
#         strings.append(pytess_to_string(img[57:103,321:500],w3,h3))
#         strings.append(pytess_to_string(img[57:103,594:773],w3,h3))
#     elif w > 900:
#         strings.append(pytess_to_string(img[57:103,47:226]))
#         strings.append(pytess_to_string(img[57:103,321:500]))
#         strings.append(pytess_to_string(img[57:103,594:773]))
#         strings.append(pytess_to_string(img[57:103,867:1046]))
#     return strings

# Moved To OCR
# def get_names_single(image,width,pos):
#     if width < 900:
#         if pos == 0:
#             return pytess_to_string(image[57:103,47:226],wtop,htop)
#         elif pos == 1:
#             return pytess_to_string(image[57:103,321:500],wtop,htop)
#         elif pos == 2:
#             return pytess_to_string(image[57:103,594:773],wtop,htop)
#     elif width > 900:
#         if pos == 0:
#             return pytess_to_string(image[57:103,47:226],wtop,htop)
#         if pos == 1:
#             return pytess_to_string(image[57:103,321:500],wtop,htop)
#         if pos == 2:
#             return pytess_to_string(image[57:103,594:773],wtop,htop)
#         if pos == 3:
#             return pytess_to_string(image[57:103,867:1046],wtop,htop)
#     return "-1"

# def get_names_bottom(image,width,pos):
#     if width < 900:
#         if pos == 0:
#             return pytess_to_string(image[310:362,47:240],wbot,hbot)
#         elif pos == 1:
#             return pytess_to_string(image[310:362,321:514],wbot,hbot)
#         elif pos == 2:
#             return pytess_to_string(image[310:362,594:787],wbot,hbot)
#     elif width > 900:
#         if pos == 0:
#             return pytess_to_string(image[310:362,47:240],wbot,hbot)
#         if pos == 1:
#             return pytess_to_string(image[310:362,321:514],wbot,hbot)
#         if pos == 2:
#             return pytess_to_string(image[310:362,594:787],wbot,hbot)
#         if pos == 3:
#             return pytess_to_string(image[310:362,867:1060],wbot,hbot)
#     return "-1"


def test_image_online(url,hash_table):
    im = url_to_image(url)
    img = im[35:45,292:362]
    hash = dhash(img)
    if hash in hash_table:
        return hash_table[hash]
    return -1

# absolute_path = os.path.join(os.getcwd(), 'card (13).jpg')
# images = cv.imread(absolute_path)
# print(images[57:103,47:226].shape[:2])
# print(images[57:103,321:500].shape[:2])
# print(images[57:103,594:773].shape[:2])
# print(images[57:103,867:1046].shape[:2])

# print(images[310:362,47:240].shape[:2])
# print(images[310:362,321:514].shape[:2])
# print(images[310:362,594:787].shape[:2])
# print(images[310:362,867:1060].shape[:2])

# print(get_names_bottom(images,1000,1))

# setup = '''
# import urllib
# import cv2 as cv
# import numpy as np
# import sys
# import os
# import argparse
# import time
# import urllib 
# import requests
# import OCR
# import timeit
# from card_image import get_names_single
# '''

# print (timeit.Timer('get_names_single(cv.imread(os.path.join(os.getcwd(), \'card (13).jpg\')),1000,0)', setup=setup).repeat(4, 15))

# print(get_names("https://media.discordapp.net/attachments/846620801456275486/851967181944127508/card.jpg?width=400&height=198"))
# url = 'https://media.discordapp.net/attachments/817563077816877116/854303894519414804/card.jpg?width=400&height=198'
# print(get_position_hash(url,hash_table('images')))
# print(test_image_online(url,hash_table('images')))
# im = url_to_image(url)
# img = im[35:45,292:362]
# cv.imshow('Cropped Image', img)
#cv.waitKey(10000)
# load_images_from_folder('images')