from dotenv import load_dotenv
import os
import requests

load_dotenv()

token = os.getenv("FACEBOOK_ACCESS_TOKEN")
page_id = "30088280604092515"
url = f"https://graph.facebook.com/v22.0/{page_id}?fields=id,posts{{message,story,created_time}}&access_token={token}"

response = requests.get(url)
data = response.json()

if "posts" in data:
    for post in data["posts"]["data"]:
        print(post.get("message") or post.get("story"))
        print(post.get("created_time"))
        print("-" * 40)
else:
    print("No posts found or an error occurred.")
