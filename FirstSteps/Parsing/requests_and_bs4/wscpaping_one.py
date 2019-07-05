import requests
from bs4 import BeautifulSoup


# page = requests.get('https://www.nga.gov/collection/artists.html') # dynamic content  :)
# soup = BeautifulSoup(page.text, 'html.parser')

def main():
    page = open('artists.html').read()  # download page
    soup = BeautifulSoup(page, 'lxml')

    # del unwanted classes
    up_links = soup.find(class_='nav-returns top')
    up_links.decompose()

    down_links = soup.find(class_='nav-returns btm')
    down_links.decompose()

    artist_name_list = soup.find('div', class_='collectionsResultListings')
    artist_name_list_items = artist_name_list.find_all('a')
    for artist_name in artist_name_list_items:
        # print(artist_name.prettify())
        names = artist_name.contents[0]  # content in tags
        print(names)
        links = artist_name.get('href')
        print(links)

    


# parsing some pages

# def some_pages():
#     pages = []
#     for i in range(1, 6):  # numbers of pages
#         url = 'http://some_site/' + str(i) + '.html'
#         pages.append(url)
#     for item in pages:
#         page = requests.get(item)
#         soup = BeautifulSoup(page.text, 'html.parser') # and so on


# if want to authorization

# headers = {
#     'User-Agent': 'Your ID, example.com',
#     'From': 'email@example.com'
# }
#
# url = 'http://example.com'
# page= requests.get(url, headers=headers)

if __name__ == '__main__':
    main()
