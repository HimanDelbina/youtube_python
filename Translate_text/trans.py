from googletrans import Translator

translator=Translator()

text = "Hello my name is himan delbina i am a programmer and live in iran kurdestan"

translation = translator.translate(text,src="en",dest='fa')
print(text)
print(translation.text)

file = open('Translate_text/text.txt','w')
file.write(translation.text)

