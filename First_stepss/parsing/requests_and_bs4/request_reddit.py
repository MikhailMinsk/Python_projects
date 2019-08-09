import requests


def get_habr():
    r = requests.get('http://habrahabr.ru')
    print(r.status_code)
    print(r.headers)
    print(r.content)


def find_pet_by_tag(tag):
    param = {'tags': tag}
    headers = {
        'Accept': 'application/xml'
        # 'Accept':'application/json'
    }
    url = 'https://www.reddit.com/r/Python/comments/bojegp/whats_everyone_working_on_this_week/'
    r = requests.get(url, params=param, headers=headers)
    print(r.status_code, r.headers)
    print(r.content)


if __name__ == '__main__':
    get_habr()
    find_pet_by_tag('string')
