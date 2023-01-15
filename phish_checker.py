import re
import requests
from bs4 import BeautifulSoup

def is_phishing(url):
    # Check the URL for spelling mistakes or variations
    match = re.match(r"(https?:\/\/)?([\w\.]+)\/?", url)
    if match:
        domain = match.group(2)
        if "." not in domain or len(domain.split(".")) > 3:
            return True
    else:
        return True
    
    # Check the website's SSL certificate
    try:
        cert = requests.get(url, verify=True)
    except requests.exceptions.SSLError:
        return True

    # Check the website's content for suspicious elements
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    if soup.find("input", {"type":"password"}) or soup.find("input", {"type":"credit"}):
        return True
    return False

def main():
    url = input("Enter a website URL to check: ")
    if is_phishing(url):
        print(f"{url} may be a phishing website.")
    else:
        print(f"{url} Not a Phishing Website")

if __name__ == "__main__":
    main()
