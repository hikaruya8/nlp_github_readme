import requests
from bs4 import BeautifulSoup

target_url = 'https://github.com/hikaruya8?tab=stars' #取得したいURL入力

def scraping_star_repo():
  r = requests.get(target_url)         #requestsを使って、webから取得
  soup = BeautifulSoup(r.text, 'lxml') #要素を抽出

  star_repo = soup.find_all("div", attrs={"class":"d-inline-block mb-1"}) #starされたリポジトリ抽出
  for link in star_repo:
    print(link.a.get('href'))

scraping_star_repo()