import requests # 웹사이트와 관련있는 모듈, 사용자의 요청을?

url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8'
res = requests.get(url)
res.raise_for_status()      # 에러가 있으면 에러 메세지를 출력하고 바로 종료, 정상이면 아래 코드를 실행
print(res.text)

