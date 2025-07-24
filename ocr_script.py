import pytesseract
from PIL import Image
import os

# Caminho do executável Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Lista de arquivos na pasta
folder_path = 'C:/Users/raiss/OneDrive/Documentos/DIGITALIZAÇÕES'
files = os.listdir(folder_path)

for file in files:
    if file.endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(folder_path, file)
        img = Image.open(img_path)
        text = pytesseract.image_to_string(img, lang='por')
        print(f'📄 Texto extraído de {file}:\n{text}\n' + '-'*50)
