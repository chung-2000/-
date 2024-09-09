import requests
from bs4 import BeautifulSoup
import sys

URL = ["https://high.deltamoocx.net/courses/course-v1:EE+EE_001+2015_08_31/pdfbook/0/"]
article = []
for index,item in enumerate(URL):
    url=(item)
    html = requests.get(url)
    sp = BeautifulSoup(html.text,"html.parser")
    dates=sp.find_all("li",class_="chapter")