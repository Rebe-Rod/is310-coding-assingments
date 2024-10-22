from bs4 import BeautifulSoup
import requests
import json 
import pandas as pd


url = 'https://over-the-garden-wall.fandom.com/wiki/Over_the_Garden_Wall_(comics_series)'

def get_comics(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    comics = soup.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color')
    comics_list = []
    for comic in comics:
        comic_title = comic.find('h3', class_='pi-data-label pi-secondary-font').text
        comic_info = comic.find('div', class_='pi-data-value pi-font').text
        comics_list.append({
            'comic_title': comic_title,
            'comic_info': comic_info
        })
    return comics_list

df = pd.DataFrame(get_comics(url))
print(df)