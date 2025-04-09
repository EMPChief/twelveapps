print("💀 Website Checker 💀")
print("Because verifying your digital choices before the internet swallows you whole is totally going to help.")

URL = input("Enter the URL of the website to check, not that it'll make a difference in the grand scheme of things: ")

if URL.startswith("https://"):
    print(
        f"🔒 Ah, using HTTPS. Someone thinks they’re safe. Adorable. The URL is valid... for now: {URL} 😏")

elif URL.startswith("http://"):
    print(
        f"🚨 Using HTTP? Bold choice. It’s like sending love letters via carrier pigeon in a war zone: {URL} 💌💣")

elif URL.startswith("www."):
    print(
        f"🌐 Ah, the good ol' 'www'—nostalgia hits different. Valid URL, but also very 2004 of you: {URL} 📼")

else:
    print(f"💔 Invalid URL detected: {URL}")
    print("Try starting with http://, https://, or www.—because the illusion of control is comforting, isn’t it? 😂")
