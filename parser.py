from bs4 import BeautifulSoup
import requests
import pandas as pd
from urllib.request import urlopen

class Parser:
    URL_SITE = "https://pogoda.mail.ru/prognoz/bryansk/"

    def pars(self):
        r = requests.get(self.URL_SITE)
        print(r)
        bs = BeautifulSoup(r.text, "html.parser")
        print(bs)
        table = bs.find('div', class_="information__content__temperature")
        print(table.text)


p = Parser()
p.pars()