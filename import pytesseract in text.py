import pytesseract
import PIL.Image
import cv2

pytesseract.pytesseract.tesseract_cmd = r'D:\college stuff\Project\Text Extractor\tesseract.exe'

myconfig = r"--psm 6 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open(r"C:\Users\daddy\Downloads\1.png"), config=myconfig)
print(text)

