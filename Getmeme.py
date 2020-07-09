from bs4 import BeautifulSoup
import requests

src=[]
def memesPage():
    index=0
    if not src:
        index+1
        Meme_New_List()
    return index

def Meme_New_List():
    meme_html=requests.get('https://memes.tw/wtf?sort=top-month&contest=11&page='+memesPage())
    soup = BeautifulSoup(meme_html.text, 'html.parser')
    img_links = soup.find_all('img','img-fluid lazy')
    for imgs in img_links:
        src.append(imgs.get('data-src'))
    memesPage()

def MemeSend():
    memesPage()
    return src.pop()
    