import os
import argparse
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv


def is_bitlink(headers, link):
    splitted_link = urlparse(link)
    without_scheme_link = '{}{}'.format(splitted_link.netloc, splitted_link.path)
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{without_scheme_link}'
    response = requests.get(api_url, headers=headers)
    return response.ok


def shorten_link(headers, link):
    request_body = {'long_url': link}
    api_url = 'https://api-ssl.bitly.com/v4/shorten'
    response = requests.post(api_url, headers=headers, json=request_body)
    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink


def count_clicks(headers, link):
    splitted_link = urlparse(link)
    without_scheme_link = '{}{}'.format(splitted_link.netloc, splitted_link.path)
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{without_scheme_link}/clicks/summary'
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()
    clicks_count = response.json()['total_clicks']
    return clicks_count


if __name__ == '__main__':
    load_dotenv()
    headers = {'Authorization': f'Bearer {os.getenv("BITLY_API_TOKEN")}'}
    parser = argparse.ArgumentParser(
        description='Сокращение ссылок'
    )
    parser.add_argument('link', help='Введите ссылку или битлинк')
    link = parser.parse_args().link
    if is_bitlink(headers, link):
        try:
            clicks_count = count_clicks(headers, link)
            print(clicks_count)
        except requests.exceptions.HTTPError:
            exit('Ошибка в ссылке')
    else:
        try:
            bitlink = shorten_link(headers, link)
            print('Битлинк', bitlink)
        except requests.exceptions.HTTPError:
            exit('Ошибка в сокращеннии ссылки')
