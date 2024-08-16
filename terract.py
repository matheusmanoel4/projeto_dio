import cv2
import pytesseract

img = cv2.imread('inputs/ia4.png')

# Usando string raw para evitar problemas com barras invertidas
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Dev\Desktop\dio\tesseract_install\tesseract.exe'
config = '--oem 3 --psm 6'
resul = pytesseract.image_to_string(img, config=config)

print(resul)
