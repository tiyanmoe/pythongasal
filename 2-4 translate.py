#install library gtranslate python
# pip install googletrans==3.1.0a0

from googletrans import Translator
tl = Translator()

text = input("masukkan text : ")

result = tl.translate(text, dest='en')

print(result.text)