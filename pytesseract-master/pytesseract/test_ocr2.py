import pytesseract
from PIL import Image

def main():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = Image.open("tests/data/test.png")
    #img.show()
    print(pytesseract.image_to_string(img, lang="eng"))


if __name__ == "__main__":
    main()