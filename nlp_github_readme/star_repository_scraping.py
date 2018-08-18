import requests
from bs4 import BeautifulSoup

target_url = 'https://github.com/hikaruya8?tab=stars' #取得したいURL入力

def scraping_star_repo():
  r = requests.get(target_url)         #requestsを使って、webから取得
  soup = BeautifulSoup(r.text, 'lxml') #要素を抽出

  star_repo = soup.find_all("div", attrs={"class":"d-inline-block mb-1"}) #starされたリポジトリ抽出
  for link in star_repo:
    repo_link = link.a.get('href')
    repo_github_link = 'https://github.com/hikaruya8{}'.format(repo_link)
    return repo_github_link

def scraping_ptag():
  r = requests.get(target_url2)         #requestsを使って、webから取得
  soup = BeautifulSoup(r.text, 'lxml') #要素を抽出

  readme_text = soup.find("article", attrs={"class":"markdown-body"}) #readme抽出
  readme_p = readme_text.find_all("p") #readme内のpタグテキスト全部抽出
  for p in readme_p:
      print(p.text)

scraping_star_repo()
target_url2 = scraping_star_repo()
scraping_ptag()