import tkinter as tk
import requests
from bs4 import BeautifulSoup
from time import sleep


display = tk.Tk()
display.title('Monitor Valut')
display.geometry("1980x1200")

Label = tk.Label(
    master=display,
    text="$$$ МОНИТОРИНГ ВАЛЮТ В БАНКАХ УКРАИНЫ $$$",
    fg="black",
    bg="red",
    width=50,
    height=3,
    font=("Times", 25)
)
Label.grid(row=0, column=1, padx=200)

Buy = tk.Label(
    master=display,
    text="BUY",
    fg="red",
    bg="black",
    width=10,
    height=2,
    font=("Times", 25)
)
Buy.grid(row=1, column=1)

Sell = tk.Label(
    master=display,
    text="SELL",
    fg="red",
    bg="black",
    width=10,
    height=2,
    font=("Times", 25)
)
Sell.grid(row=1, column=2, pady=20)



bank_1 = tk.Label(
    text="Pumb dollars",
    fg="red",
    bg="black",
    width=10,
    height=3,
    font=("Arial",20)
)
bank_1.grid(row=2, column=0)

buy_dollar_1 = tk.Label(
    master=display,
    text="",
    fg="red",
    bg="black",
    width=10,
    height=2,
    font=("Times", 25)
)
buy_dollar_1.grid(row=2, column=1)

sell_dollar_1 = tk.Label(
    master=display,
    text="",
    fg="red",
    bg="black",
    width=10,
    height=2,
    font=("Times", 25)
)
sell_dollar_1.grid(row=2, column=2)

bank_2 = tk.Label(
    text="Privat dollars",
    fg="red",
    bg="black",
    width=10,
    height=3,
    font=("Arial",20)
)
bank_2.grid(row=3, column=0, pady=50)

buy_dollar_2 = tk.Label(
    master=display,
    text="",
    fg="red",
    bg="black",
    width=10,
    height=2,
    font=("Times", 25)
)
buy_dollar_2.grid(row=3, column=1)

sell_dollar_2 = tk.Label(
    master=display,
    text="",
    fg="red",
    bg="black",
    width=10,
    height=2,
    font=("Times", 25)
)
sell_dollar_2.grid(row=3, column=2)

def monitoring_pumb():
    url_punb = 'https://about.pumb.ua/ru/info/currency_converter'
    r_pumb = requests.get(url_punb)
    soup_pumb = BeautifulSoup(r_pumb.text, 'lxml')
    buy = soup_pumb.find('div', class_='content').find('div', class_='exchange-rate').findAll('tr')[1].findAll('td')[1].text
    sell = soup_pumb.find('div', class_='content').find('div', class_='exchange-rate').findAll('tr')[1].findAll('td')[2].text
    buy_dollar_1.config(
        text=buy
    )
    sell_dollar_1.config(
        text=sell
    )
    display.after(3000, monitoring_pumb)


def monitoring_privat():
    url_privat = 'https://privatbank.ua/rates-archive#archive-block'
    r_private = requests.get(url_privat)
    soup_private = BeautifulSoup(r_private.text, 'lxml')
    buy = soup_private.findAll('div', class_='currency-pairs')[1].find('div', class_='purchase').text
    sell = soup_private.findAll('div', class_='currency-pairs')[1].find('div', class_='sale').text
    buy_dollar_2.config(
        text=buy
    )
    sell_dollar_2.config(
        text=sell
    )

    display.after(3000, monitoring_privat)
display.after(1000, monitoring_pumb)
display.after(1000, monitoring_privat)

display.mainloop()