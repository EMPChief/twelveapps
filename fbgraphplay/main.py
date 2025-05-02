from dotenv import load_dotenv
import os
import requests
load_dotenv()

token = os.getenv("FACEBOOK_ACCSESS_TOKEN")
url = f"https://graph.facebook.com/v22.0/me?fields=id%2Cname&access_token={token}"

req = requests.get(url)
print(req.content)