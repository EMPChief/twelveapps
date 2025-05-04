from dotenv import load_dotenv
import os
import requests

load_dotenv()

token = os.getenv("FACEBOOK_ACCESS_TOKEN")
page_id = "30088280604092515_28843693078551280"
url = f"https://graph.facebook.com/v22.0/{page_id}/photos?fields=link,picture&access_token={token}"

response = requests.get(url)
data = response.json()
print(data)
