#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException

import csv
import datetime
import subprocess

def get_html(url):
    try:
        response = requests.get(url)
        return response.text
    except RequestException:
        raise

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    spans = soup.find_all("span", class_="ipsKurs_rate")
    values = []
    for span in spans:
        values.append(span.text)
    return values

def write_info(path, data):
    with open(path, "a") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow((data,))

def log(data=""):
    with open(".log", "ab") as file:
        data_string = "{0}{1}\n".format(
            data,
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        file.write(data_string.encode())

def show_notification(title, text):
    subprocess.call('notify-send "{0}" "{1}"'.format(title, text), shell=True)

def main():
    URL = "https://kurs.com.ua/"
    try:
        html = get_html(URL)
    except RequestException as e:
        time = datetime.datetime.now()
        log("RequestException - ")
        return None
    info = parse_html(html)
    USD = info[0]
    EUR = info[6]
    show_notification("Exchange rate USD, EUR", "USD - {0}\nEUR - {1}".format(USD, EUR))
    write_info("USD.csv", USD)
    write_info("EUR.csv", EUR)

if __name__ == "__main__":
    main()
