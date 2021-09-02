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
from tesseract_ocr import *

class TestOCRCheck(unittest.TestCase):
    def setUp(self):
        self.ocr = OCR_PyTes()
        
    def tearDown(self) -> None:
        self.ocr.depose()
        del self.ocr

    def test_card1(self):
        absolute_path = os.path.join(os.getcwd(), 'card (1).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
        
    def test_card2(self):
        absolute_path = os.path.join(os.getcwd(), 'card (2).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
    
    def test_card3(self):
        absolute_path = os.path.join(os.getcwd(), 'card (3).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
        
    def test_card4(self):
        absolute_path = os.path.join(os.getcwd(), 'card (4).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=10000)
        
    def test_card5(self):
        absolute_path = os.path.join(os.getcwd(), 'card (5).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
        
    def test_card6(self):
        absolute_path = os.path.join(os.getcwd(), 'card (6).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertEqual(self.ocr.get_print_num(images,1),10)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
    
    def test_card7(self):
        absolute_path = os.path.join(os.getcwd(), 'card (7).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertEqual(self.ocr.get_print_num(images,2),10)
        
    def test_card8(self):
        absolute_path = os.path.join(os.getcwd(), 'card (8).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)

    def test_card9(self):
        absolute_path = os.path.join(os.getcwd(), 'card (9).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,2)==1000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=10000)        

    def test_card10(self):
        absolute_path = os.path.join(os.getcwd(), 'card (10).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)

    def test_card11(self):
        absolute_path = os.path.join(os.getcwd(), 'card (11).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        
    def test_card12(self):
        absolute_path = os.path.join(os.getcwd(), 'card (12).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        
    def test_card13(self):
        absolute_path = os.path.join(os.getcwd(), 'card (13).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=1000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        
    def test_card14(self):
        absolute_path = os.path.join(os.getcwd(), 'card (14).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=10000)
        
    def test_card15(self):
        absolute_path = os.path.join(os.getcwd(), 'card (15).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
    
    def test_card16(self):
        absolute_path = os.path.join(os.getcwd(), 'card (16).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=1000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
        
    def test_card17(self):
        absolute_path = os.path.join(os.getcwd(), 'card (17).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=1000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        
    def test_card18(self):
        absolute_path = os.path.join(os.getcwd(), 'card (18).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=10000)
        
    def test_card19(self):
        absolute_path = os.path.join(os.getcwd(), 'card (19).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
        
    def test_card20(self):
        absolute_path = os.path.join(os.getcwd(), 'card (20).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=1000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
        
    def test_card21(self):
        absolute_path = os.path.join(os.getcwd(), 'card (21).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=10000)
        
    def test_card22(self):
        absolute_path = os.path.join(os.getcwd(), 'card (22).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        
    def test_card23(self):
        absolute_path = os.path.join(os.getcwd(), 'card (23).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=10000)
        
    def test_card24(self):
        absolute_path = os.path.join(os.getcwd(), 'card (24).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=1000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        
    def test_card25(self):
        absolute_path = os.path.join(os.getcwd(), 'card (25).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
        
    def test_card26(self):
        absolute_path = os.path.join(os.getcwd(), 'card (26).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)==100)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
        
    def test_card27(self):
        absolute_path = os.path.join(os.getcwd(), 'card (27).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
        
    def test_card28(self):
        absolute_path = os.path.join(os.getcwd(), 'card (28).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
        
    def test_card29(self):
        absolute_path = os.path.join(os.getcwd(), 'card (29).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        
    def test_card30(self):
        absolute_path = os.path.join(os.getcwd(), 'card (30).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=1000)
        
    def test_card31(self):
        absolute_path = os.path.join(os.getcwd(), 'card (31).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=1000)
        
    def test_card32(self):
        absolute_path = os.path.join(os.getcwd(), 'card (32).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        
    def test_card33(self):
        absolute_path = os.path.join(os.getcwd(), 'card (33).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
        
    def test_card34(self):
        absolute_path = os.path.join(os.getcwd(), 'card (34).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
        
    def test_card35(self):
        absolute_path = os.path.join(os.getcwd(), 'card (35).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
        
    def test_card36(self):
        absolute_path = os.path.join(os.getcwd(), 'card (36).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
    
    def test_card37(self):
        absolute_path = os.path.join(os.getcwd(), 'card (37).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
    
    def test_card38(self):
        absolute_path = os.path.join(os.getcwd(), 'card (38).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=1000)
        
    def test_card39(self):
        absolute_path = os.path.join(os.getcwd(), 'card (39).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=1000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
    
    def test_card40(self):
        absolute_path = os.path.join(os.getcwd(), 'card (40).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)==10)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
        
    def test_card41(self):
        absolute_path = os.path.join(os.getcwd(), 'card (41).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
        
    def test_card42(self):
        absolute_path = os.path.join(os.getcwd(), 'card (42).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
        
    def test_card43(self):
        absolute_path = os.path.join(os.getcwd(), 'card (43).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)

    def test_card44(self):
        absolute_path = os.path.join(os.getcwd(), 'card (44).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=1000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)     
        
    def test_card45(self):
        absolute_path = os.path.join(os.getcwd(), 'card (45).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=10000)
        
    def test_card46(self):
        absolute_path = os.path.join(os.getcwd(), 'card (46).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=10000)
        
    def test_card47(self):
        absolute_path = os.path.join(os.getcwd(), 'card (47).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        
    def test_card48(self):
        absolute_path = os.path.join(os.getcwd(), 'card (48).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)==100)
        
    def test_card49(self):
        absolute_path = os.path.join(os.getcwd(), 'card (49).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=1000)
    
    def test_card50(self):
        absolute_path = os.path.join(os.getcwd(), 'card (50).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=10000)
        
    def test_card51(self):
        absolute_path = os.path.join(os.getcwd(), 'card (51).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
        
    def test_card52(self):
        absolute_path = os.path.join(os.getcwd(), 'card (52).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)==100)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
        
    def test_card53(self):
        absolute_path = os.path.join(os.getcwd(), 'card (53).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)==100)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000) 
        
    def test_card54(self):
        absolute_path = os.path.join(os.getcwd(), 'card (54).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)==100)
        
    def test_card55(self):
        absolute_path = os.path.join(os.getcwd(), 'card (55).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=10000)
        
    def test_card56(self):
        absolute_path = os.path.join(os.getcwd(), 'card (56).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
        
    def test_card57(self):
        absolute_path = os.path.join(os.getcwd(), 'card (57).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)==10)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)

    def test_card58(self):
        absolute_path = os.path.join(os.getcwd(), 'card (58).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)

    def test_card59(self):
        absolute_path = os.path.join(os.getcwd(), 'card (59).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)==100)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
        
    def test_card60(self):
        absolute_path = os.path.join(os.getcwd(), 'card (60).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)

    def test_card61(self):
        absolute_path = os.path.join(os.getcwd(), 'card (61).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)==10)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)

    def test_card62(self):
        absolute_path = os.path.join(os.getcwd(), 'card (62).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
        
    def test_card63(self):
        absolute_path = os.path.join(os.getcwd(), 'card (63).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)


    def test_card64(self):
        absolute_path = os.path.join(os.getcwd(), 'card (64).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=10000)
        
    def test_card66(self):
        absolute_path = os.path.join(os.getcwd(), 'card (66).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=1000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
    
    def test_card67(self):
        absolute_path = os.path.join(os.getcwd(), 'card (67).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=1000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        
    def test_card68(self):
        absolute_path = os.path.join(os.getcwd(), 'card (68).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=1000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=100000)
    
    def test_card69(self):
        absolute_path = os.path.join(os.getcwd(), 'card (69).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,3)>=1000)
        
    def test_card82(self):
        absolute_path = os.path.join(os.getcwd(), 'card (82).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
        
    def test_card83(self):
        absolute_path = os.path.join(os.getcwd(), 'card (83).png')
        images = cv2.imread(absolute_path)
        self.assertTrue(self.ocr.get_print_num(images,0)>=10000)
        self.assertTrue(self.ocr.get_print_num(images,1)>=100000)
        self.assertTrue(self.ocr.get_print_num(images,2)>=100000)
    
if __name__ == '__main__':
    unittest.main()