import requests
import csv
from time import sleep
from random import randint

from bs4 import BeautifulSoup


file = open('mouses.csv', 'w', encoding='utf-8', newline='\n')
file_csv = csv.writer(file)
file_csv.writerow(['url, name_of_product'])

ind = 1

while ind < 8:
    try:

        url = f'https://pcroom.ge/kategoria/periperialebi/mausi/page/{ind}/'
        r = requests.get(url)

        soup_all = BeautifulSoup(r.text, 'html.parser')
        soup = soup_all.find('div', class_='products')
        mouses = soup.find_all('div', class_='product-grid-item')

        for each in mouses:
            url = each.img.attrs.get("src")
            name_of_product = each.h3.a.text
            file_csv.writerow([url, name_of_product])
    except:
        print('')
    ind += 12
    sleep(randint(2, 5))







