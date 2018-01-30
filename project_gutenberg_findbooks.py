from bs4 import BeautifulSoup
import requests
import pandas


categories = []
url = "https://www.gutenberg.org/wiki/Category:Bookshelf"
r = requests.get(url)
c = r.content
soup = BeautifulSoup(c, 'html.parser')
category_lists = soup.findAll('div', {'id': 'mw-pages'})
for gen in category_lists:
	for cat in gen.findAll('li'):
		for cat1 in cat.findAll('a'):
			categories.append(cat1.text)

for category in categories:
	print(category)


search = input('Enter the category name you want to search from the above list: ')
search = search.replace(' ' , '_')

book_data = []

url = 'https://www.gutenberg.org/wiki/' + search
r = requests.get(url)
c = r.content
soup = BeautifulSoup(c, 'html.parser')
search_page = soup.findAll('div', {'id': 'bodyContent'})
description = []
for des in search_page:
	description.append(des.find('p').text)
print(description)

'''
for information in search_page:
	info = {}
	for data in information.findAll('ul'):
		for data1 in data.findAll('li'):
			print(data1.find('a', {'class': 'extiw'}))
		book_data.append(info)

print(book_data)

'''
	

