# https://stackoverflow.com/questions/432385/sftp-in-python-platform-independent
# cd C:/Users/lzmi1/PycharmProjects/PDF_TO_SFTP
from PyPDF2 import PdfFileReader


def test_pdf(path):
   # creating an object
   path = 'pdf/plik_testowy.PDF'
   path1 = 'pdf/plik_testowy2.pdf'
   file = open(path, 'rb')

   # creating a pdf reader object
   filereader = PdfFileReader(file)
   # print the number of pages in pdf file
   print(filereader.numPages)


def text_extractor(path, page_num):
   with open(path, 'rb') as f:
      pdf = PdfFileReader(f)
      # get the first page
      page = pdf.getPage(page_num)
      # print(page)
      # print('Page type: {}'.format(str(type(page))))
      text = page.extractText()
   return text


def find_text_first_position(char_to_find_text):
   """Procedure to find text inside string and return first position of this text"""
   return txt.find(char_to_find_text)


def find_text_last_position(text_to_find, base_text):
   pos = base_text.find(text_to_find) + len(text_to_find)
   """Procedure to get last pos of string inside text"""
   return pos


def take_text_from_to(text, pos_start, pos_end):
   """Taking text from specific position inside text to specific position"""
   return text[pos_start:pos_end]


def take_text_from_to_plus(txt, char_start, margin_start, char_count, end_spaces):
   """Taking text from specific position inside text to specific position"""
   return txt[char_start + margin_start:char_count + end_spaces]

def load_content_pdf(self, path):
   pdf_text = text_extractor(path, 0)
   tresc_pdf = pdf_text
   return tresc_pdf