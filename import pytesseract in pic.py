import pytesseract
import cv2
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'D:\college stuff\Project\Text Extractor\tesseract.exe'

myconfig = r"--psm 11 --oem 3"

img_path = r"D:\college stuff\Project\Text extract py\x.jpg"
img = cv2.imread(img_path)

if img is not None:
    height, width, _ = img.shape

    data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)

    amount_boxes = len(data['text'])
    for i in range(amount_boxes):
        if float(data["conf"][i]) > 80:
            (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)
            img = cv2.putText(img, data['text'][i], (x, y + height + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0),
                              2, cv2.LINE_AA)

    cv2.imshow("image", img)
    cv2.waitKey(0)
else:
    print(f"Failed to load the image: {img_path}")
