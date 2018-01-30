from bs4 import BeautifulSoup
import requests
import pandas


genres = []
url = "http://www.imdb.com/feature/genre"
r = requests.get(url)
c = r.content
soup = BeautifulSoup(c, 'html.parser')
genre_lists = soup.findAll('div', {'class':'aux-content-widget-2'})
    
for gen in genre_lists:
	for gen1 in gen.findAll('div',{'class':'ab_links'}):
		for cat in gen1.findAll('a'):
			genres.append(cat.text)

list.sort(genres)
print(genres)