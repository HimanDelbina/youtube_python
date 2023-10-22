import pyttsx3
from PyPDF2 import PdfReader


engine = pyttsx3.init()

reader = PdfReader('pdf_to_audio/book.pdf')
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
file = open('pdf_to_audio/text.txt','w')
file.write(text)
print(text)

engine.save_to_file(text,'story.mp3')
engine.runAndWait()



# #insert name of your pdf 
# book = open('pdf_to_audio/book.pdf','rb')
# pdfreader = PdfReader(book)
# speaker = pyttsx3.init()

# for page_num in range(pdfreader.numPages):
#     text = pdfreader.getPage(page_num).extractText()
#     clean_text = text.strip().replace('\n', ' ')
#     print(clean_text)
# #name mp3 file whatever you would like
# speaker.save_to_file(clean_text, 'story.mp3')
# speaker.runAndWait()

# speaker.stop()