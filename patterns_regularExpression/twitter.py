import re
#re.sub(pattern, replace, string, count=0, flags=0)
# i.e)  re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

#prompt users for the URL of their twitter profile and get from it the user's, user name

url = input("URL: ").strip()
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))

