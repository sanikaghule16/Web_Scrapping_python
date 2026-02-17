import re
import requests
def isValidURL(url):
    regex = r"((http|https)://)(www.)?[a-zA-Z0-9@:%._\+~#?&//=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%._\+~#?&//=]*)"
    return re.fullmatch(regex, url)is not None
def scrape_urls(website_url):
    try:
        response=requests.get(website_url)
        html=response.text
        url_pattern=r'https?://[^\s"<>]+'
        urls=re.findall(url_pattern,html)
        return(set(urls))
    except Exception as e:
        print("error")
        return[]
# Driver Code
if __name__ == "__main__":
    url = "https://smbstcollege.edu.in/"
    
    if isValidURL(url):
        print("Valid URL\n Scrapping links...\n")
        links=scrape_urls(url)
        for link in links:
            print(link)
    else:
        print("Invalid URL")
