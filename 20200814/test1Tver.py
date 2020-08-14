from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
from pathlib import Path

url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8'

res = requests.get(url)
# print(res.text, len(res.text))

res.raise_for_status()      # 만약 에러가 있으면 에러 메세지 출력 후 끝내고 아니면 하위에 코드를 실행

soup = bs(res.text,'lxml')
# pprint(soup)

dds = soup.find_all('dd',attrs={'class':'lv1'})
pprint(dds)

for d in dds:
    # print(d)        # <dd class="lv1"><span class="num">22㎍/㎥</span>좋음<span class="ico"></span></dd>            
    num = d.find('span',attrs={'class':'num'})
    # print(num)        # <span class="num">22㎍/㎥</span>
    print(num.get_text())
    print('---------------------------')
# 정의 목록 만들기
# <dl> 정의 목록(definition List)
#   <dt> 용어 제목 </dt>(definition term)
#   <dd> 용어 설명 </dd>(definition description)

# span :컨텐츠를 감쌀 만큼의 공간만 차이 -> div는 화면 왼쪽부터 오른쪽끝까지 전부 차지함

temp = soup.find('span',attrs={'class':'todaytemp'})
# pprint(temp)
pprint(temp.get_text())
print('---------------------------')

rainfall = soup.find('span',attrs={'class':'rainfall'})
pprint(rainfall)
num = rainfall.find('span',attrs={'class':'num'})
pprint(num.get_text())