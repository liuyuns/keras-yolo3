
import pytesseract
import os

from PIL import ImageFilter

print ('old cmd path', pytesseract.pytesseract.tesseract_cmd)

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

print ('new cmd exists: ', os.path.exists(pytesseract.pytesseract.tesseract_cmd))

def process_image(image):
    text = pytesseract.image_to_string(image)

    print('text:', text)
    return text