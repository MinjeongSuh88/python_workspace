from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
from pathlib import Path

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}

url = 'https://comic.naver.com/webtoon/detail.nhn?titleId=20853&no=1237&weekday=tue'
res = requests.get(url)       # 이 url로 가서 가져와
res.raise_for_status()      # 상태를 보고 문제가 없으면 res를 일으켜
# if res.status_code ==200:
#     실행..
# else:
#     에러..

# pprint(res.text)      # '\t\t\t\tnaver.comic.oArtistAction = new naver.comic.Artist();\r\n'
soup = bs(res.text,'lxml')     # 불필요한 것을 모두 제거
# pprint(soup)      # \t 이런거 전부 빠짐

data = soup.find('div',attrs={'class':'wt_viewer'})
# pprint(data)       # <div class="wt_viewer" style="background:#FFFFFF"><img alt="comic content" class="" ~

images = data.find_all('img')
for img in images:
    pprint(img['src'])      # 키 값이 src인 것 가져옴
    path = img['src']
    # res2 = requests.get(path)
    # print(res2)     # 반복 프로그램이 요청하면 403 :접근할 권한이 없음
# 웹브라우저임을 가장하여 네이버에 요청 -> 브라우저의 유저 에이전트 값을 받아옴
    res2 = requests.get(path,headers=headers)       # 접근하는 애가 크롬인 척 가장
    # print(res2)
    # print(path[46:50])
    Path('./img/'+path[46:50]).mkdir(parents=True,exist_ok=True)
    with open('./img/'+path[46:50]+'/'+path[-12:],'wb') as f:      # 사진은 바이너리 형식
        f.write(res2.content)