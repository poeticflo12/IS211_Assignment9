#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment9 - Scraping Web Pages with BeautifulSoup - Apple Stock.
Tested in Python 2.7.15
"""

import urllib.request
from bs4 import BeautifulSoup
import json
import html.parser

url = 'http://www.nasdaq.com/market-activity/stocks/aapl/historical '
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read())


def apple_stock():
    data = []
    fhandler = soup.find_all('tr')

    for rows in fhandler:
        try:
            if len(rows.find_all(('td', {'class': 'span data-reactid'}))) == 7:
                date = rows.contents[0].get_text()
                close = rows.contents[5].get_text()
                data.append((date, close))
                json_string = {
                    "Date": date,
                    "Closed Stock Price": close,
                }
                print(json.dumps(json_string))
        except:
            print
            'bad url'
            continue
    return apple_stock


if __name__ == "__main__":
    apple_stock()