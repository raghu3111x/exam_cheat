from docx import Document
import PyPDF2
import pyfiglet
import webbrowser
import time 

# doc = Document('sample.docx')

# for para in doc.paragraphs:
# 	print(para.text)
pdf_name = input('Enter the pdf file name: ')
pdf_file_object = open(pdf_name,'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file_object)
n = pdf_reader.numPages
for i in range(n):
	print(pyfiglet.figlet_format(text='Page Number   ' + str(i+1)))
	print('\n')
	global page_obj,text
	page_obj = pdf_reader.getPage(i)
	text = page_obj.extractText()
	ques = text.split('?')
	num = len(ques)
	for a in range(num):
		webbrowser.open(url='https://www.google.com/search?q=' + ques[a])
	_next = input(':')
	if _next.lower() =='next':
		pass
	else:
		time.sleep(1000000)
		
print(pyfiglet.figlet_format(text='Thanks for using ! '))
