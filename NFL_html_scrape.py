#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 12:39:45 2024

@author: ahmeds
"""

import requests
from bs4 import BeautifulSoup

import pandas as pd

url = 'https://www.nfl.com/standings/league/2019/PRE'


page = requests.get(url)
page 

soup = BeautifulSoup(page.text, 'lxml')
soup

table = soup.find('table', {'summary':'Standings - Detailed View'})
table

# getting the HTML of the headers
table.find_all('th')

headers = []
for i in table.find_all('th'):
    title = i.text.strip()
    headers.append(title)

# putting the headers in the dataframe
df = pd.DataFrame(columns = headers)

    
# getting the body of the table
for j in table.find_all('tr')[1:]:
    first_td = j.find_all('td')[0].find('div', class_ = 'd3-o-club-fullname').text.strip()
    row_data = j.find_all('td')[1:]
    row = [tr.text for tr in row_data]
    row.insert(0, first_td)
    length = len(df)
    df.loc[length] = row
    
    