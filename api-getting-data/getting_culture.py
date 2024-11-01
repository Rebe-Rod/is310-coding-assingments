import requests
import os
import pandas as pd
import apikey
import json

europeana_api_key = apikey.load("EUROPEANA_API_KEY")
os.environ['EUROPEANA_API_KEY'] = europeana_api_key

def get_quotes(query):
    url = f"https://favqs.com/api/quotes/:quote_id"

    response = requests.get("url")
    quote_data = response.json()
    quote_data = {
        "quote": quote_data['quote']['body'],
        "author": quote_data['quote']['author'],
        "id": quote_data['quote']['id']
    }

def search_europeana(query):
        url = f"https://api.europeana.eu/record/v2/search.json?wskey={os.environ['EUROPEANA_API_KEY']}&query={query}"
        response = requests.get(url)
        data = response.json()
        return data

def main():
   get_quotes = get_quotes()
   if not get_quotes:
         print("No quotes found")
         return

with open ('quotes.json', 'w') as f:
    json.dump(get_quotes, f, indent=2)

print("Quotes saved to quotes.json")