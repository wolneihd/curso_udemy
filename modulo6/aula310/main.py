# python -m http.server -d modulo6/aula310/
# 
# PS C:\Users\f0fp0228\Desktop\Curso DEV\curso_udemy\modulo6> python -m http.server -d aula310/ 3333
# Serving HTTP on :: port 3333 (http://[::]:3333/) ...
# ::1 - - [11/Jul/2024 13:16:02] "GET / HTTP/1.1" 200 -
# ::1 - - [11/Jul/2024 13:16:02] "GET /style.css HTTP/1.1" 200 -
# 
# http://  =>  80
# https:// => 443 
# 
# pip install bs4
#
# https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/

import requests
from bs4 import BeautifulSoup

url = 'http://localhost:3333/'
response = requests.get(url)
raw_html = response.text
parse_html = BeautifulSoup(raw_html, 'html.parser')

#print(response)
#print(response.headers)
#print(response.text)

top_job_heading = parse_html.select_one('#intro > div > div > article > h2')
print(top_job_heading.text) 

if top_job_heading is not None:
    article = top_job_heading.parent
    #print(article)
    if article is not None:
        for p in article.select('p'):
            print(p.text)