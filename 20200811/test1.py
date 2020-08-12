# web Crawling :여러 사이트를 정지적으로 돌며 정보를 추출하는 기술
# ==> DB

# web Scraping :웹사이트에서 특정 정보를 추출하는 기술
 
# HTML, CSS, Javasript 

import requests # 웹사이트와 관련있는 모듈, 사용자의 요청을?

res = requests.get('http://m.naver.com')        # 이 사이트로 가서 페이지를 얻어온 것
print(res)      # <Response [200]>  
print('응답코드 :',res.status_code)     
# 200 :정상(HTTP.status)
# 404 :찾을 수 없는 페이지 -> url 오류, 403 :권한 없음
# url(uniform resource location)
# 500 :서버 사이드 로직 에러

if res.status_code == requests.codes.ok:      # 정상 코드 200 대신 상수로 만들어놓은 값 -> 숫자만 써놓으면 나중에 왜 써놨는지 모를까봐
    print(len(res.text))

res.raise_for_status()      # 에러가 있으면 에러 메세지를 출력하고 바로 종료, 정상이면 아래 코드를 실행

#  파일로 저장
with open('google.html','w',encoding = 'utf-8') as f:
    f.write(res.text)

