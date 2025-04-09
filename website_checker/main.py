print("🌐 Website Checker")

URL = input("Enter the URL of the website to check: ")
if URL.startswith("https://"):
    print(f"🔒 https is a secure protocol so the URL is valid: {URL} 👍")

elif URL.startswith("http://"):
    print(
        f"⚠️ http is an insecure protocol so the URL is valid tough it is not secure: {URL} 😬")

elif URL.startswith("www."):
    print(f"🌐 www is a subdomain so the URL is valid: {URL} 👌")

else:
    print(f"🚫 The URL is invalid: {URL}")
    print("Please enter a valid URL starting with http://, https://, or www. 😊")
