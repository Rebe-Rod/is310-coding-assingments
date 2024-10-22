from bs4 import BeautifulSoup
import requests
import json 
import pandas as pd
from rich.console import Console
import os

console = Console()

url = 'https://over-the-garden-wall.fandom.com/wiki/Over_the_Garden_Wall_(comics_series)'

def get_comics(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    comics = soup.find_all('tabel', class_='wikitable')
    comics_list = []

    for comic in comics:
        comic_title = comic.find_all('a', class_='wikitable').text
        comic_info = comic.find_all('td', class_='wikitable').text
        comics_list.append({
            'comic_title': comic_title,
            'comic_info': comic_info
        })
        comics_list.append([comic_info.get_text(strip=True) for comic_info in comic.find_all('td')])
        comics_list.append([comic_title.get_text(strip=True) for comic_title in comic.find_all('a')])
    return comics_list

cwd = os.getcwd()
with open('over_the_garden_wall.json', 'w') as file:
    json.dump(get_comics(url), file, indent=2)
    file_path = os.path.join(cwd, 'over_the_garden_wall.json')
console.print(f"\n[bold yellow]Your data has been saved to {file_path}![/bold yellow]")