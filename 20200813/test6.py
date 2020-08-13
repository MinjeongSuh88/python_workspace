from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
from pathlib import Path

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}

for i in range(1230,1237):
    url = 'https://comic.naver.com/webtoon/detail.nhn?titleId=20853&no={}&weekday=tue'.format(i)        # {} 자리를 변수 처리
    res = requests.get(url)       # 이 url로 가서 가져와
    res.raise_for_status()      # 상태를 보고 문제가 없으면 res를 일으켜

    soup = bs(res.text,'lxml')     # 불필요한 것을 모두 제거

    data = soup.find('div',attrs={'class':'wt_viewer'})

    images = data.find_all('img')
    for img in images:
        pprint(img['src'])      # img태그의 속성src인 것 가져옴
        path = img['src']
        res2 = requests.get(path,headers=headers)       # 접근하는 애가 크롬인 척 가장
        Path('./img/'+path[46:50]).mkdir(parents=True,exist_ok=True)
        with open('./img/'+path[46:50]+'/'+path[-12:],'wb') as f:      # 사진은 바이너리 형식
            f.write(res2.content)