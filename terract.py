import cv2
import pytesseract

# Carregar a imagem
img = cv2.imread(r'C:\Users\Dev\Desktop\dio\projeto_dio\inputs\ia4.png')

#caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Configurações do Tesseract
config = '--oem 3 --psm 6'

# Realizar OCR na imagem
resul = pytesseract.image_to_string(img, config=config)

print(resul)