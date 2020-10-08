"""
Exercise from: https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html
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
    with open('file_to_save.txt', 'w') as open_file:
        for title in titles:
            open_file.write(title.text + "\n")


if __name__ == "__main__":
    run()