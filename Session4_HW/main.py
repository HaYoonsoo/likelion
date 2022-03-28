import requests
import csv
from bs4 import BeautifulSoup
from extract import extract_info

WT_URL = "https://comic.naver.com/webtoon/weekdayList?week=mon"
wt_html = requests.get(WT_URL)
wt_soup = BeautifulSoup(wt_html.text, "html.parser")
wt_list_box = wt_soup.find("ul", {"class":"img_list"})
wt_list = wt_list_box.find_all("li")
result = extract_info(wt_list)

file = open('webtoon_mon.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(['title', 'author', 'rating'])

for i in range(result['length']):
    writer.writerow([result['title'][i], result['author'][i], result['rating'][i]])
    print(result['title'][i], result['author'][i], result['rating'][i])