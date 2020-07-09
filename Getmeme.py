from bs4 import BeautifulSoup
import requests

src=[]
index=0
def memesPage():
    if not src:
        index=index+1
        Meme_New_List(index)
    if index==36:
        index=0

def Meme_New_List(page):
    meme_html=requests.get('https://memes.tw/wtf?sort=top-month&contest=11&page=%s'%(page))
    soup = BeautifulSoup(meme_html.text, 'html.parser')
    img_links = soup.find_all('img','img-fluid lazy')
    for imgs in img_links:
        src.append(imgs.get('data-src'))
    memesPage()

def MemeSend():
    memesPage()
    return src.pop()