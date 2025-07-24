import pytesseract
from pdf2image import convert_from_path
from pathlib import Path

# === CONFIGURAÇÕES ===
poppler_path = r"C:\Program Files\poppler-xx\bin"  # <-- ajuste se necessário
tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# === CAMINHOS ===
base_path = Path(__file__).resolve().parent.parent
input_path = base_path / "input"
output_path = base_path / "output"
output_path.mkdir(exist_ok=True)

# === LOOP DE PDFs ===
for file in input_path.glob("*.pdf"):
    print(f"📄 Extraindo de: {file.name}")
    pages = convert_from_path(str(file), dpi=300, poppler_path=poppler_path)
    
    texto_total = ""
    for i, page in enumerate(pages):
        text = pytesseract.image_to_string(page, lang="por")
        texto_total += f"\n\n--- Página {i+1} ---\n{text}"
    
    # SALVA COMO .TXT
    txt_file = output_path / f"{file.stem}.txt"
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(texto_total)
    
    print(f"✅ Texto salvo em: {txt_file.name}")


