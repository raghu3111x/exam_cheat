from bs4 import BeautifulSoup
import requests
import webbrowser as wb
import random



global url_links
global titles
global pretty_links

global preshnn_list

preshnn_list = []


url_links = []
titles = []
pretty_links = []

url = input("Enter the url: " + '\n')

html_text = requests.get(url).text
soup = BeautifulSoup(html_text,'lxml')
boom = soup.find('div')
ques = boom.text.replace('____','?').split('?')
print(ques)
for q in ques:


	global m_list 
	m_list = []
	separated = list(q)
	for i in range(len(separated)):
		if separated[i].isnumeric()==True:
			m_list.append(i)

	try:
		preshnn_list.append(q[m_list[1]:])
		# print(q[m_list[1]:])
		# print('\n')
	except:
		pass

for i in range(len(preshnn_list)):
    
    query = preshnn_list[i]
    url = 'https://www.google.com/search?client=firefox-b-d&q=' + query
    wb.open(url)
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
        if 'google' in url_links[i]:
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
        y = random.randint(0, len(pretty_links) - 1)
        print(pretty_links[y])
        wb.open(pretty_links[y])
