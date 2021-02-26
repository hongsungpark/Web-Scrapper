from Indeed import extract_indeed_pages, extract_indeed_jobs

#Indeed의 last 페이지 넘버 가져오기
last_indeed_pages = extract_indeed_pages()

#Indeed 모든 페이지 job 정보 가져오기
extract_indeed_jobs(last_indeed_pages)