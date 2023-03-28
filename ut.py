import random 
import string
from faker import Faker
import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

def get_password(length: int = 10) -> str:
    
    ppassword = ''
    chars = string.ascii_letters + string.digits + string.punctuation
    for _ in range(length):
        ppassword += random.choice(chars)
    return ppassword

def get_requirements() -> str:
    with open('requirements.txt','r') as g:
        text = g.read()
        
    return text

def get_generate_users(max_users: int = 50) -> str:
    name = ''
    gmail = ''
    chars = string.ascii_lowercase

    for e in range(max_users):
        fake = Faker()
        
        
        for i in range(random.randint(5,10)):
            gmail += random.choice(chars)

        name += f'\n{e+1}. {fake.name()} {gmail}@gmail.com\n'
        gmail = ''    
    return name


def get_space():
    r = requests.get('http://api.open-notify.org/astros.json')
    return r.json()['number']
    


# url = 'https://kinokrad.cc/'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
# link = soup.find('div', class_='shorbox').find('div', class_='postertitle').find('a').get('href')
# name = soup.find('div', class_='shorbox').find('div', class_='postertitle').find('a').text
# opisanie = soup.find('div', class_='shorbox').find('div', class_='shorttext').text
# country = soup.find('div', class_='shorbox').findAll('span', class_='orange')[1].text
# resisor = soup.find('div', class_='shorbox').findAll('span', class_='orange')[3].text
# janr = soup.find('div', class_='shorbox').findAll('span', class_='orange')[2].text

# reitings = soup.find('div', class_='imdb').text

# data = []
# for p in range(1,6):
#     print(p)
#     url = f'https://kinokrad.cc/page/{p}/'
#     r = requests.get(url)
#     sleep(3)
#     soup = BeautifulSoup(r.text, 'lxml')

#     films = soup.findAll('div', class_='shorbox')

#     for film in films:
#         link = film.find('div', class_='postertitle').find('a').get('href')
#         name = film.find('div', class_='postertitle').find('a').text
#         country = film.findAll('span', class_='orange')[1].text
#         resisor = film.findAll('span', class_='orange')[3].text
#         janr = film.findAll('span', class_='orange')[2].text
        
#     # reiting = film.find('div', class_='imdb')

#         data.append([name, country, resisor,janr, link])

# print(data)
# header = ['name', 'country', 'resisor','janr', 'link']

# df = pd.DataFrame(data, columns=header)
# df.to_csv('C:/dsf/kinopoisc_data.csv.txt', sep=';', encoding='utf-8')