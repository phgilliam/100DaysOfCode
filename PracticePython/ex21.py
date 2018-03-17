import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
article = soup.find_all(class_='story-heading')
headlines = [x.find('a') for x in article]
headlines = filter(None, headlines)
headlines = [x.string for x in headlines]

with open('headlines.txt','w') as f:
        for x in headlines:
                f.write('x' + '\n')
        f.close()
