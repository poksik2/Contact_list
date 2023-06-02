from bs4 import BeautifulSoup
import requests
import pandas as pd
from urllib.request import urlopen

class Parser:
    URL_SITE = "https://pogoda.mail.ru/prognoz/bryansk/"

    def pars(self):
        r = requests.get(self.URL_SITE)
        bs = BeautifulSoup(r.text, "html.parser")
        table = bs.find('div', class_="information__content__temperature")
        print('Сейчас за окном',table.text.strip())
        tible1 = bs.find('span', title="Ощущается как +23°")
        print(tible1.text.strip())

p = Parser()
p.pars()