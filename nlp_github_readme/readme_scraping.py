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
  for p in readme_p: #readme textリスト化
    list_url.append(p.text)
  return list_url
  # for n,p in enumerate(readme_p):
  #   print(p.text)
    # if n ==3: #止めたい時
    #   break

def tokenize():
  tokens = scraping_ptag()
  for t in tokens:
    words_split = nltk.word_tokenize(t)
    print(words_split)
    words_tag = nltk.pos_tag(words_split)
    print(words_tag)

tokenize()


