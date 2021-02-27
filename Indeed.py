import requests  #get html data
from bs4 import BeautifulSoup  #html parser

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=devops&limit={LIMIT}"


def get_last_page():
    #indeed 쿼리 페이지의 html 가져오기
    result = requests.get(URL)
    #bs객체에 넣기(html 파서 선택)
    soup = BeautifulSoup(result.text, "html.parser")

    #조회된 첫페이지 이후 마지막 페이지까지 조회하기 위해 마지막 페이지 숫자를 찾아내야 한다
    #페이지 정보 가져오기 위해서 해당 클래스 추출(웹에서 html소스 '검사'로 조회해서 클래스명 확인))
    pagination = soup.find("div", {"class": "pagination"})
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


def extract_jobs(html):
    #job title 리스트 저장
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    #기업 리스트 저장
    company = html.find("span", {"class": "company"})
    #company class에 anchor 가 있는 것 없는 것 다르게 처리하는 분기문
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    # company 양옆에 개행, 공백이 있어서 strip으로 제거 후 저장
    company = company.strip()
    #location = html.find("span", {"class": "location"}).string
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {
        'title': title,
        'company': company,
        'location': location,
        'link': f"https://kr.indeed.com/채용보기?jk={job_id}"
    }


def extract_jobs_allpage(last_page):
    jobs = []
    #마지막 페이지 번호만큼 requests 수행해서 job title 가져오기
    for page in range(last_page):
      print(f"Scrapping page {page}")
      result = requests.get(f"{URL}&start={page*LIMIT}")
      soup = BeautifulSoup(result.text, "html.parser")
      # 채용공고 부분 html 객체 results에 저장
      results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
      for result in results:
          job = extract_jobs(result)
          jobs.append(job)
    return jobs

def get_jobs():
    #Indeed의 last 페이지 넘버 가져오기
    last_page = get_last_page()
    #Indeed 모든 페이지 job 정보 가져오기
    jobs = extract_jobs_allpage(last_page)
    return jobs