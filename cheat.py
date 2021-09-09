import pyperclip
from docx import Document
import PyPDF2
import pyfiglet
import webbrowser as wb
import time 
import os 
import pyttsx3
from bs4 import BeautifulSoup
import requests
import random


#import spacy


url_links = []
titles = []
pretty_links = []
valid_imgs_link = []


global ques
ques = ''


#nlp = spacy.load('en_core_web_sm')
# doc = Document('sample.docx')

# for para in doc.paragraphs:
# 	print(para.text)

engine = pyttsx3.init('sapi5')


def say(x):
	engine.say(x)
	engine.runAndWait()


def serp_api():
    global url_links
    global titles
    global pretty_links
    #global valid_imgs_link
    global ques
    url = 'https://www.google.com/search?client=firefox-b-d&q=' + ques
    html_text = requests.get(url=url).text
    soup = BeautifulSoup(html_text, 'lxml')
    links = soup.find_all('a')

    for link in links:
        if link.find('h3'):  # selecting only those which have meaningful title
            boom = link.find('h3')
            url_links.append(link['href'])
            titles.append(boom.text)

        # if link['href'].startswith('/search?client'):
        #     pass
        # else:
        #     try:
        #         boom = link.find('h3')
        #         # print(boom.text + ' : ' + link['href'])
        #         url_links.append(link['href'])
        #         titles.append(boom.text)
        #     except:
        #         pass

    # if len(url_links) == len(titles):
    #     print(f'title: {len(titles)} url_links: {len(url_links)}')
    #     for i in range(len(titles)):
    #         print(
    #             '[*]' + titles[i] + '       -----------     ' + url_links[i], end='\n\n\n'
    #         )

    # getting clean links
    for i in range(len(url_links)):
        if 'google' in url_links[i] or 'youtube' in url_links[i] or 'facebook' in url_links[i]:
            pass
        else:
            if url_links[i].startswith('/url?q='):
                pretty_link = (
                    url_links[i]
                    .replace('/url?q=', '')
                    .split('&sa=')[0]
                    .replace(f'%3Fv%3D', '?v=')
                )
                # print(f'[*] {titles[i]}')
                # print('google.com' + url_links[i])
                # print()
                pretty_links.append(pretty_link)

    for i in range(1):
        y = random.randint(0, len(pretty_links))
        print(pretty_links[y])
        wb.open(pretty_links[y])
        # html_text1 = requests.get(pretty_links[y]).text
        # soup1 = BeautifulSoup(html_text, 'lxml')
        # imgs = soup1.find_all('img')
        # try:
        #     if ques.lower() in imgs['alt'].replace(' ', '').lower():
        #         valid_imgs_link = valid_imgs_link.append('https:' + imgs['source'])

        # except:
        #     print('Sorry Sir, No images found.')

        # for i in range(min(1, len(valid_imgs_link))):
        #     wb.open(valid_imgs_link[i])


pdf_loc = 'c:\\users\\RS21\\Documents'
pdf_files_list = []
files = os.listdir(pdf_loc)
for file in files:
	if file.endswith('.pdf'):
		pdf_files_list.append(file)
	else:
		pass
print()
for i in range(len(pdf_files_list)):
	print(str(int(i+1)) + ' ' + pdf_files_list[i])
say('Enter the pdf file name sir !')
name = input('Enter the pdf file name sir !')
pdf_loc = pdf_loc +'\\' + name
pdf_file_object = open(pdf_loc,'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file_object)
n = pdf_reader.numPages
#say("Here you go sir !")
reversed_range = range(n, 0, -1)

for i in reversed_range:

#for i in range(n):
	#print(pyfiglet.figlet_format(text='Page Number   ' + str(i+1)))
	print('\n')
	global page_obj,text
	page_obj = pdf_reader.getPage(i - 1 ) 
	text = page_obj.extractText()
	# doc = nlp(text)
	# global string
	# string = ''
	# for token in doc:
	# 	string += ' ' + token.text
	# print('string == ' + string)
	# sense = string.split('\n')
	# print(sense[1])
	
	lines = text.replace('\n\n',' ').split('\n')
	#print(lines)
	for i in range(len(lines)-1):
		if lines[i] == '' or lines[i] == '':
			pass

		elif lines[i][0].isdecimal() == True or lines[i][0] == 'i' or lines[i][0].lower() == 'q':
			ques = lines[i] + lines [i+1]
			if '?' in ques:
				pass
			else:
				ques +=lines[i+2]
				if '?' not in ques:
					ques += lines[i+3]
					if '?' not in ques:
						ques += lines[i+4]
			serp_api()
			# for i in range(len(lines)):
			# 	if '?' in ques:
			# 		pass
			# 	else:
			# 		ques += lines[i]
			# print(ques)



# 	ques = text.split('?')
# 	for i in range(len(ques)):
# 		print(ques[i].replace('\n',' ').replace('\\n',' ').replace('.','&&'))
# 		wb.open('https://www.google.com/search?q=' + ques[i])
	

			
# print(pyfiglet.figlet_format(text='Thanks for using ! '))
print()
print()
