#! /usr/bin/python3

'''
    Author of this program: Doula Isham Rashik
    Date Published: 14/09/2017

	Note: Only to be used for educational purposes.

	Description: This program allows to download all pdf files automatically from a certain web page.

	Input: Link of the web page from which pdf links to be extracted
	Output: Downloaded pdf files in the folder
'''

# All the required libraries are imported
import requests, re
from bs4 import BeautifulSoup


# Inputs from the user
full_url = input('Enter url link from which pdf files to be downloaded: ')


# Checks domain name
def checks_for_domain(main_url):
    if '.org/' in main_url:
        return main_url[:main_url.find('.org/') + len('.org/') - 1]
    elif '.edu/' in main_url:
        return main_url[:main_url.find('.edu/') + len('.edu/') - 1]
    else:
        return main_url[:main_url.find('.com/') + len('.com/') - 1]


# This function allows to open HTML file and parse it followed by extracting .pdf links
def get_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', href=re.compile('([A-Za-z0-9_:()])+'))
    pdflink =[]

    for link in links:
        if '.pdf' in re.findall(".pdf", link['href']):
            pdflink.append(link['href'])

    return pdflink

# Allows downloading of pdf files using extracted .pdf links
def download():
    pdflinks = get_url(full_url)
    serverName = checks_for_domain(full_url)
    lengthOfpdflinks = len(pdflinks)

    for i in range(lengthOfpdflinks):
        if pdflinks[i].startswith('/.'):
            res = requests.get(serverName + pdflinks[i][len('/.'):])
        elif pdflinks[i].startswith('http://') or pdflinks[i].startswith('https://'):
            res = requests.get(pdflinks[i])
        else:
            res = requests.get(serverName + pdflinks[i])

        playFile = open('File' + str(i) + '.pdf', 'wb')

        for chunk in res.iter_content(len(res.text)):
            playFile.write(chunk)

        playFile.close()

download()

