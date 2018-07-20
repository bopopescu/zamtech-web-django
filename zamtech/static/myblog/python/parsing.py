from bs4 import BeautifulSoup
import requests

url = 'http://sarjana.jteti.ugm.ac.id/akademik/'

r = requests.get(url)
html_contents = r.text

html_soup = BeautifulSoup(html_contents, "html.parser")

header1 = html_soup.find('h1')

content1 = html_soup.find('table', class_='table table-hover table-pad')


print(header1.text)
print(content1.text)