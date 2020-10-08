"""
Exercise from: https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
Code created by Ruben Jimenez
"""
import requests
from bs4 import BeautifulSoup


def run():
    url = 'https://www.nytimes.com/'
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html,"html.parser")
    titles = soup.find_all('h3')
    for title in titles:
        print(title.text)


if __name__ == "__main__":
    run()