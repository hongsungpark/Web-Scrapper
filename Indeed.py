import requests #get html data
from bs4 import BeautifulSoup #html parser

INDEED_URL = "https://kr.indeed.com/jobs?q=devops&limit=50"

def extract_indeed_pages():
  #indeed 쿼리 페이지의 html 가져오기
  result = requests.get(INDEED_URL)
  #bs객체에 넣기(html 파서 선택)
  soup = BeautifulSoup(result.text, "html.parser")

  #조회된 첫페이지 이후 마지막 페이지까지 조회하기 위해 마지막 페이지 숫자를 찾아내야 한다
  #페이지 정보 가져오기 위해서 해당 클래스 추출(웹에서 html소스 '검사'로 조회해서 클래스명 확인))
  pagination = soup.find("div", {"class":"pagination"})

  #클래스 내의 anchor(a)들을 리스트로 할당
  links = pagination.find_all('a')

  #anchor 내부의 spans를 담을 리스트
  pages = []

  #spans의 string 값(페이지 번호)을 int로 저장(마지막 next를 뺴기 위해 -1까지)
  for link in links[:-1]:
    pages.append(int(link.string))

  #마지막 페이지 번호를 변수에 저장
  max_page = pages[-1]
  return max_page

