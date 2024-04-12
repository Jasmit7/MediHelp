from paddleocr import PaddleOCR, draw_ocr
import cv2
import os
from drug_named_entity_recognition import find_drugs

class OCR:
    def __init__(self):
        self.ocr_model = PaddleOCR(lang='en')

    @staticmethod
    def keep_unique_words(input_str):
        words = input_str.split()
        unique_words = set(words)
        return ' '.join(unique_words)
    
    def get_medicine_name(self, img_path):
        result = self.ocr_model.ocr(img_path)
        medicine_names = []
        for item in result:
            for _, (medicine_name, confidence) in item:
                medicine_names.append(medicine_name)
        img_text = ' '.join(medicine_names)
        result = OCR.keep_unique_words(img_text)
        drug_info = find_drugs(result.split(" "))
        return drug_info

    
