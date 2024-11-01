import apikey
import os

apikey.save("EUROPEANA_API_KEY", "eurpoena_api_key")
os.environ['EUROPEANA_API_KEY'] = eurpoena_api_key

import pyeuropeana.apis as apis

#response = apis.search(query="Galadriel")
#for item in response['items']:
    #print(item['guid'])

response = apis.entity.suggest(
    text = 'Eritrea',
    TYPE = 'place',
)
print(response)