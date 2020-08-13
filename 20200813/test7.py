from bs4 import BeautifulSoup as bs     # 스프 임포트
from pprint import pprint       # pprint       
import requests     # url에 응답 요청하는 모듈
from pathlib import Path

url = 'https://movie.naver.com/movie/running/current.nhn'

res = requests.get(url)     # url로부터 반응 받음
res.raise_for_status()      # url의 반응이 정상(200)이면 일으킴
# pprint(res.text)      # \t 등이 다 찍혀 나옴

soup = bs(res.text,'lxml')      # url의 내용을 lxml로 해석하여 soup변수에 담음
# pprint(soup)        # \t 등 걸러냄

divs = soup.find_all('div',attrs={'class':'thumb'})     # div태그에 class속성 값이 thumb인 것을 모두 찾음
# # pprint(divs)

idx = 0
for div in divs:
    # pprint(div)
    # print('------------------------------')
    aTag = div.find('a')
    # pprint(aTag['href'][28:])        # href속성에서 28번째 자리부터 끝까지
    movieNo = aTag['href'].split('=')[1]        # '='기준으로 나눈 것의 두번째꺼 영화번호 가져와도 됨
    url2 = 'https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode='+movieNo      # https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode=190447
    # print(url2)
    res2 = requests.get(url2)       # url2의 반응을 res2변수에 담음
    # pprint(res2)      # <Response [200]>       
    soup2 = bs(res2.text,'lxml')
    img = soup2.find('img')
    # print(img['src'])       
    imgpath = img['src']        # img의 url까지 확보
    res3 = requests.get(imgpath)

    Path('./img/movie_poster').mkdir(parents=True,exist_ok=True)     # 해당 경에 폴더 만듦
    idx += 1
    with open('./img/movie_poster/movie{}.jpg'.format(idx),'wb') as f:        
        f.write(res3.content)
