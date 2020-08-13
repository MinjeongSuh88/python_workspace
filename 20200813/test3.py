# 외부 데이터 가져오기
import requests      # 리모트에 있는 데이터에 접근하기
from bs4 import BeautifulSoup as bs
from pprint import pprint

url = 'https://comic.naver.com/webtoon/list.nhn?titleId=20853'
res = requests.get(url)       # 주소창에 요청해 가져오기
res.raise_for_status()
res.close()     # 항상 자원 사용 후 끊어줘야 함
# pprint(res.text)      # print보다 더 보기 쉽게 나옴

# 가져올 목표 정함
soup = bs(res.text,'lxml')      # 이 글자를 해석기로 해석함
# print(soup,type(soup))     # 이상한 문자가 정리되어 있음, <class 'bs4.BeautifulSoup'>
print(soup.title)       # 해당 페이지의 제목이 나옴, <title>마음의소리 :: 네이버 만화</title>
print(soup.title.get_text())       # 태그 사이의 텍스트만 가져옴, 마음의소리 :: 네이버 만화

print('---------------------------------------------------')
# find 다음에는 태그 이름 명시 가능
print(soup.find('a'))      # soup 객체에서 처음 발견되는 a element 출력
print('---------------------------------------------------')
print(soup.a.attrs)     # a태그의 속성들만, {'href': '#menu', 'onclick': "document.getElementById('menu').tabIndex=-1;document.getElementById('menu').focus();return false;"} -> 딕셔너리 형식으로 출력
print('---------------------------------------------------')
print(soup.a.attrs['href'])        # soup의 a태그의 속성 href의 값만 가져옴

print('---------------------------------------------------')
# 제목 전부를 찾고 싶을 경우
tdList = soup.find_all('td',attrs={'class':'title'})      # td태그에서 속성 class가 title인 것들을 모두 찾음
# print(tdList,type(tdList))
# print(tdList[0].find('a').get_text())
for i in tdList:
    print(i.find('a').get_text())



