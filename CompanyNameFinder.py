#! /usr/bin/python3

'''
    Author of this program: Doula Isham Rashik
    Date Published: 14/09/2017

    Note: Only to be used for educational purposes.

    Description: This piece of program allows to obtain the names of the companies
    in UAE within a specific city from yellow pages.

    Input: Keyword/Catagory, maximum number of pages to be scraped, City
    Output: List of company names from specific city
'''

# Importing modules that will allow access to the webpages
import requests
from bs4 import BeautifulSoup


# Definition of function that takes in user inputs
def inputs():
    search = input("Enter Keywords: ")
    max_pages = int(input("Enter maximum pages to be scraped: "))
    city = input("Enter City: ")
    get_pages(search, max_pages, city)


# Definition of function to enter the yellow page webpages and extracts company names
def get_pages(keyword, max_pages, city):
    companies = []

    for i in range(max_pages):
        url = "http://yellowpages.ae/s/" + city + "/" + keyword + "-" + str(i) + "-1.html"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')
        g_data = soup.find_all("section", {"class": "left"})

        for item in g_data:
            companies.append(item.contents[3].text.strip(' '))

    out = input("\nDisplay the companies in terminal[T/t] or store and save them in a file[S/s]? ")
    i = 1

    if out == 'T' or out == 't':
        print('\nList of companies in ' + city + ' as follows: \n')
        for company in companies:
            print(str(i) + '. ' + company)
            i += 1

    elif out == 'S' or out == 's':
        playFile = open(keyword + '-companies-' + city + '.txt', 'w')
        playFile.write('\nList of companies in ' + city + ' as follows: \n\n')
        for company in companies:
            playFile.write(str(i) + '. ' + company + '\n')
            i += 1
        playFile.close()


# Definite loop to check if the user wants to obtain company names again
while True:
    inputs()
    prompt = input("\nDo you want to continue[Y/y] or quit the program[N/n]? ")
    if prompt == "N" or prompt == "n":
        break
