import requests
import re
from app.main import write_json


def parse_text(text):
    pattern = r'/\w+'
    crypto = re.search(pattern, text).group()
    return crypto[1:]


def get_price(crypto):
    url = 'https://api.coinmarketcap.com/v2/ticker/{}'.format(crypto)
    r = requests.get(url).json()
    price = r['data']['quotes']['USD']['price']
    return price


def main():
    # print(get_price())
    print(get_price(parse_text('how much is /1?')))


if __name__ == '__main__':
    main()
