from Indeed import get_jobs as get_indeed_jobs
from save import save_to_file

# Web Scrapping
indeed_jobs = get_indeed_jobs()
# Writing a file
save_to_file(indeed_jobs)

