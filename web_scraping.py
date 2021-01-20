import requests
import bs4
import re

def get_text(html_url):
    html = requests.get(html_url).text
    soup = bs4.BeautifulSoup(html, "html.parser")
    
    for script in soup(["script", "style"]):
        script.decompose()

    text = soup.get_text()
    lines= [line.strip() for line in text.splitlines()]
    text="\n".join(line for line in lines if line)

    #文字列を返す
    return text

def get_slash_text(html_url):
    html = requests.get(html_url).text
    soup = bs4.BeautifulSoup(html, "html.parser")
    
    for script in soup(["script", "style"]):
        script.decompose()

    text = soup.get_text('/')
    lines= [line.strip() for line in text.splitlines()]
    text="\n".join(line for line in lines if line)

    #文字列を返す
    return text