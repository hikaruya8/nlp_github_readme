import requests
from bs4 import BeautifulSoup
import nltk

target_url = 'https://github.com/nltk/nltk' #取得したいURL入力

def scraping_ptag():
  r = requests.get(target_url)         #requestsを使って、webから取得
  soup = BeautifulSoup(r.text, 'lxml') #要素を抽出

  readme_text = soup.find("article", attrs={"class":"markdown-body"}) #readme抽出
  readme_p = readme_text.find_all("p") #readme内のpタグテキスト全部抽出
  list_url = []
  for p in readme_p:
    list_url.append(p.text)
  return list_url
  # for n,p in enumerate(readme_p):
      # print(n, p.text)
      # if n ==3: #止めたい時
      #   break

def tokenize():
  tokens = nltk.word_tokenize(scraping_ptag())
  text = nltk.Text(tokens)

scraping_ptag()
# tokenize()


