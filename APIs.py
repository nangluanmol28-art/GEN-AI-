# W3D3
# for create the VN first go to folder (cd LANDCHAIN) 
# (python -m venv myenv)
# new folder (myenv) created
# creating txt file of requirements in the langchain folder 
# activate the VN (myenv/scripts/activate)
# install libraries (pip install -r requirements.txt)

# requests -


# API - application programming interface 

# get
# post
# update - put
# delete

# newsapi.org
# after getting api key create the .env 

import requests
from dotenv import load_dotenv
import os 

load_dotenv()
api = os.getenv('API_KEY')
query = input("Enter Your Query:")
url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api}"

result = requests.get(url)
data = result.json()
# print(data)
# first_article = data['articles'][0]
# print(first_article.keys())
# print(first_article["title"])
# print(first_article["description"])

for article in range(10):
    print(f"Headline {article+1}: {data['articles'][article]['title']} ")
