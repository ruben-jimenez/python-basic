"""
Exercise from: https://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html
Code created by Ruben Jimenez
"""

import requests
from bs4 import BeautifulSoup


def run():
    url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html,"html.parser")
    content = soup.select('div.body__container p')
    for paragraph in content:
        print(paragraph.text)


if __name__ == "__main__":
    run()