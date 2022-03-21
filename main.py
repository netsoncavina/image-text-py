import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\netso\Documents\Programação\Projetos\Python\Tesseract\tesseract.exe'
from PIL import Image

img = Image.open('teste.png')
img2 = Image.open('image.png')
text = tess.image_to_string(img)
text2 = tess.image_to_string(img2)
string = ""
numbers = ['1','2','3','4','5','6','7','8','9','0']
signs = ['-']
for letter in text:
    if letter not in numbers:
        if letter in signs:
            string += letter
        else:
            string += " "
    else:
        string += letter

number = int(string[5:7])
print(text)
# print(text2)

