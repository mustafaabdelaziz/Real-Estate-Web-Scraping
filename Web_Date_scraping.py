# importing libraries.
import pandas as pd
import datetime
from bs4 import BeautifulSoup
import requests
import re
import csv
import os
from dotenv import load_dotenv


# Loading User Agent from enviornment variables.
load_dotenv()
User_Agent = os.getenv('USER_AGENT') 



headers = {"User-Agent": User_Agent }


# Creating a function to get HTML data from webpage.
def getdata(URL):
    r = requests.get(URL,headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


# Creating a function to get all pages from a page.
def getpages(soup, URL):
    page = soup.find_all('a', {'data-testid':'pagination-page-next-button'})
    if page != None:
            page = os.getenv("BASE_SITE_URL") + page[len(page)-2]["href"] 
            return page
    else:
        return

# Getting all pages for the website.
last_page = 0
initial_URL = os.getenv("INITIAL_URL") # Getting the initial URL from the environemnt variables. 
URL = initial_URL
pages = [initial_URL]
while(True):
    soup = getdata(URL)
    URL = getpages(soup, URL)
    # max_page = int(URL[-1])
    # if max_page > last_page:
    #     last_page = max_page
    # else:
    #     break
    pages.append(URL)

# Creating lists of features.
title_c = {"id":[],"title":[]}
address_c = {'id':[], 'address':[]}
price_c = {"id":[],"price":[]}
space_cleaned = {"id":[],"space_m2":[]}
rooms_c = {"id":[],"rooms":[]}
bathrooms_c = {"id":[],"bathrooms":[]}
id = 0

# Grapping the data of the features from all pagees.
for page in pages:
    soup = getdata(page)
    titles = soup.find_all('h2')
    prices = soup.find_all('p', {'data-testid':'property-card-price'})
    spaces_m2 = soup.find_all('p', {'data-testid' : 'property-card-spec-area'} )
    rooms = soup.find_all('p', {'data-testid' : 'property-card-spec-bedroom'} )
    bathrooms = soup.find_all('p', {'data-testid' : 'property-card-spec-bathroom'} )
    addresses = soup.find_all('div', {'data-testid' : 'property-card-location'} )

    # Cleaning the data before adding them to the lists.
    for title, price, space, room, bathroom, address in zip(titles, prices, spaces_m2, rooms, bathrooms, addresses):
        title_c['id'].append(id) 
        title_c['title'].append(title.get_text().strip())

        address = address.find('p').get_text().strip()
        address_c['id'].append(id)
        address_c['address'].append(address)

        price = price.get_text().strip()[:-4]
        price = price.replace(',', '')
        price = price.replace('\n', '')
        price = price.replace('Ask for p', '')
        if price == '':
            price = 0
        price_c['id'].append(id) 
        price_c['price'].append(int(price))

        space = space.get_text().strip()
        # space = re.sub("[^A-Za-z0-9]","",space)[:-1]
        space_cleaned["id"].append(id)
        space_cleaned['space_m2'].append(space)

        room = room.get_text().strip()
        rooms_c['id'].append(id)
        rooms_c['rooms'].append(room)

        bathroom = bathroom.get_text().strip()
        bathrooms_c['id'].append(id)
        bathrooms_c['bathrooms'].append(bathroom)
        id += 1


# writing the data into a csv file.
header = ['id', 'title', 'address', 'price', 'space_sqm', 'rooms', "bathrooms"]
with open("real estate data.csv", "a+", newline='', encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for id, title, address, price, space, rooms, bathrooms in zip(title_c['id'], title_c['title'], address_c['address'], price_c['price'], space_cleaned['space_m2'], rooms_c['rooms'], bathrooms_c['bathrooms']):
        writer.writerow([id, title, address, price, space, rooms, bathrooms])




