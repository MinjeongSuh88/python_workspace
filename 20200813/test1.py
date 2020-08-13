# 외부 데이터 가져오기
import requests      # 리모트에 있는 데이터에 접근하기

url = 'https://comic.naver.com/webtoon/list.nhn?titleId=20853'
res = requests.get(url)       # 주소창(네이버 웹툰)에 요청해 가져온 응답을 res변수에 담음
res.raise_for_status()      # 해당 페이지가 정상이면 일으켜
res.close()
# print(res)      
# print(res.status_code)        # 200, 해당 페이지의 여부
# print(res.text)     # html 문서를 출력