import pytesseract
from pdf2image import convert_from_path
import os

# Caminhos
folder_path = 'C:/Users/raiss/OneDrive/Documentos/DIGITALIZAÇÕES'
poppler_path = r'C:\Program Files\poppler-xx\bin'  # Altere para seu caminho real
tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Altere para seu Tesseract

# Configurações
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# Percorrer PDFs da pasta
for file in os.listdir(folder_path):
    if file.lower().endswith('.pdf'):
        pdf_path = os.path.join(folder_path, file)
        print(f'📄 Extraindo de: {file}')

        # Converte PDF em imagens (uma por página)
        pages = convert_from_path(pdf_path, 300, poppler_path=poppler_path)

        for i, page in enumerate(pages):
            text = pytesseract.image_to_string(page, lang='por')
            print(f'\n📄 Página {i+1} do {file}:\n{text}')
            print('-' * 60)

from pathlib import Path

# Criando estrutura de pastas do projeto
base_path = Path.cwd()
folders = ['input', 'output', 'scripts', 'logs']

for folder in folders:
    (base_path / folder).mkdir(exist_ok=True)

# Criando arquivos padrões
readme = (base_path / "README.md")
gitignore = (base_path / ".gitignore")
requirements = (base_path / "requirements.txt")


