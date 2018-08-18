import requests
from bs4 import BeautifulSoup

target_url = 'https://github.com/hikaruya8?tab=stars' #取得したいURL入力

def scraping_star_repo():
  r = requests.get(target_url)         #requestsを使って、webから取得
  soup = BeautifulSoup(r.text, 'lxml') #要素を抽出

  star_repo = soup.find_all("div", attrs={"class":"d-inline-block mb-1"}) #starされたリポジトリ抽出
  list_repo_link = []
  for link in star_repo:
    repo_link = link.a.get('href')
    repo_github_link = 'https://github.com{}'.format(repo_link)
    list_repo_link.append(repo_github_link)
  return list_repo_link

def scraping_ptag():
  for x in range(5):
    if x == 1:
      break
    print(x)
    for target_url2 in scraping_star_repo():
      l = requests.get(target_url2)         #requestsを使って、webから取得
      soup = BeautifulSoup(l.text, 'lxml') #要素を抽出
      readme_text = soup.find("article", attrs={"class":"markdown-body"}) #readme抽出
      readme_p = readme_text.find_all("p") #readme内のpタグテキスト全部抽出
      for p in readme_p:
        print(p.text)

scraping_ptag()