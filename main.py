import requests #get html data
from bs4 import BeautifulSoup #html parser

#indeed 쿼리 페이지 html 가져오기
indeed_result = requests.get("https://kr.indeed.com/jobs?q=devops&limit=50")

#bs객체에 넣기(html 선택)
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

#페이지 정보 가져오기 위해서 해당 클래스 추출
pagination = indeed_soup.find("div", {"class":"pagination"})

#클래스 내의 anchor 리스트로 할당
pages = pagination.find_all('a')

#anchor 내부의 spans를 담을 리스트
spans = []

#spans 저장
for page in pages:
  spans.append(page.find("span"))

#페이지 숫자들 외에 마지막 화살표 제외하기 위해 인덱스 조정
print(spans[0:-1])
