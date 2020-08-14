# 클래스의 이름을 모르거나 찾기 어려울 경우 => selenium
# 웹 브라우저의 자동화를 가능하게 하는 다양한 도구와 라이브러리 포함하는 프로젝트

# webdriver 필요함
# 브라우저 버전 확인 :주소창에 'chrome://version' 검색하면 나옴 -> 84.0.4147.125

from selenium import webdriver      # 주소창에 크롬드라이버 검색 후 첫번째 사이트에서 84-윈도우 버전 다운로드
from selenium.webdriver.common.keys import Keys
import time

# 크롬 드라이버 객체 생성
brower = webdriver.Chrome("e:/dev/python_workspace/chromedriver.exe")      # 현재 워크 스페이스에 실행 파일있으므로 경로 생략
                                 # 만약 다른 경로에 있다면 괄호 안에 파일명까지 경로 명시해주어야 함
# 브라우저 객체로 네이버 웹페이지 접속                                 
brower.get('http://naver.com')      # 파이썬에서 웹브라우저를 강제로 실행시킴

# 검색창 엘리먼트 객체
element = brower.find_element_by_id('query')        # 네이버 검색창의 id가 query임
element.click()     # 창을 띄운 후 검색창에 클릭이 됨
element.send_keys('택배 없는 날')       # 검색창에 해당 검색어가 보내짐
element.send_keys(Keys.ENTER)       # Keys 클래스 임포트해와서 엔터키 
# button = brower.find_element_by_id('search_btn')        
# button.click()

# brower.quit()

time.sleep(3)
brower.get('http://google.com') #3초 후 구글로 이동
element = brower.find_element_by_name('q')      # 검색창 엘리먼트 만듦
element.click()
element.send_keys('광복절')
element.send_keys(Keys.ENTER)
time.sleep(3)

element.click()
element.send_keys(Keys.BACKSPACE)       # 지웠다가 재검색
element.send_keys(Keys.BACKSPACE)       
element.send_keys(Keys.BACKSPACE)       
element.send_keys('휴일')
element.send_keys(Keys.ENTER)
