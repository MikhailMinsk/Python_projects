from bs4 import BeautifulSoup
import re

reg = r'\d{2}.\d{2}.\d{4}'
# reg = r'\w\-' r'*post'  r'\d{}$'

def main():
    html = open('index.html').read()
    soup = BeautifulSoup(html, 'lxml')

    div = soup.find('div', class_='links')  # find first blog /div
    # div = soup.find('div', {'class': 'links', 'id': 'ad'})

    links = div.find_all('a')  # soup objects
    for i in links:
        print(i)
        link = i.get('href')
        print(link)  # only link

    # parent = find_parent()  # same find, but down up
    # parents = find_parents()  # same find_all, but down up
    #
    # div = soup.find('h1').find_parent()
    # print(div)
    # div = soup.find('h1').find_parents('div')
    # print(div)

    text = soup.find('h1').next_element.next_element  # return next element by the list
    text = soup.find('h1').next_sibling  # previous_sibling - down up
    print(text)

    # re

    a = soup.find('a', href=re.compile('some text to find'))
    a = a.get('href')  # only link

    a = soup.find('a', href=re.compile('bing.com$'))  # return first link ; $ - do not wait any char after text
    a = soup.find('a', text=re.compile('one'))
    a = soup.find('div', text=re.compile(reg))


if __name__ == '__main__':
    main()