import requests
from bs4 import BeautifulSoup

target_url = 'https://github.com/nltk/nltk' #取得したいURL入力

def scraping_ptag():
  r = requests.get(target_url)         #requestsを使って、webから取得
  soup = BeautifulSoup(r.text, 'lxml') #要素を抽出

  readme_text = soup.find("article", attrs={"class":"markdown-body"}) #readme抽出
  readme_p = readme_text.find_all("p") #readme内のpタグテキスト全部抽出
  for p in readme_p:
      print(p.text)

scraping_ptag()
