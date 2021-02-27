import csv

def save_to_file(jobs):
  # write only mode로 파일 생성
  file = open("jobs.csv", mode="w")
  writer = csv.writer(file)
  # 첫행 입력
  writer.writerow(["title", "company", "location", "link"])
  for job in jobs:
    # Dictionary 중 value 값들만 가져오고 list 로 변환하여 입력
    writer.writerow(list(job.values()))
  return