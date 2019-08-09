import requests
from bs4 import BeautifulSoup

url = 'https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'
page = requests.get(url)

print(page.status_code)
# print(page.text)
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.prettify())
print(soup.find_all('p'))  # return list
print('\n\n\n')
print(soup.find_all('p')[2])  # second string of list
print('\n\n\n')
print(soup.find_all(class_='chorus'))  # return all in class 'chorus'
print('\n\n\n')
