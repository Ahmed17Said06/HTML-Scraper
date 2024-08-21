#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 21:44:33 2024

@author: ahmeds
"""
# imports

import requests
from bs4 import BeautifulSoup

import pandas as pd

url = 'https://www.worldometers.info/world-population'


page = requests.get(url)
page 

soup = BeautifulSoup(page.text, 'lxml')
soup

# getting the HTML of the whole table
table = soup.find('table', class_ = 'table table-striped table-bordered table-hover table-condensed table-list')
table

# getting the HTML of the headers
table.find_all('th')

# setting the setting the headers
headers = []
for i in table.find_all('th'):
    title = i.text
    headers.append(title)
    
# putting the headers in the dataframe
df = pd.DataFrame(columns = headers)

# getting the body of the table
for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [tr.text for tr in row_data]
    length = len(df)
    df.loc[length] = row
    
# saving the table into .csv
df.to_csv('./table_html_scraped.csv')
    
    
    
