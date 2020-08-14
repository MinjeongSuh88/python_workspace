from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
from pathlib import Path

url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8'

res = requests.get(url)
res.raise_for_status()      

soup = bs(res.text,'lxml')
# pprint(soup)

# 온도 뽑아내기
tt = soup.find('span',attrs={'class':'todaytemp'})
print(tt.get_text())

# 강수량 뽑아내기
rf = soup.find('span',attrs={'class':'rainfall'})
print(rf.find('span',attrs={'class':'num'}).get_text())

# 미세먼지 뽑아내기
lv1 = soup.find('dd',attrs={'class':'lv1'})
# print(lv1)

