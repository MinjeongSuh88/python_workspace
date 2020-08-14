from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 코레일 열차표 예매
brower = webdriver.Chrome('e:/dev/python_workspace/chromedriver.exe')
brower.get('http://www.letskorail.com')

# print(brower.window_handles)        # 팝업 목록 확인, ['CDwindow-AADFD94E5D86BFB6151C8BFD1D5127F6', 'CDwindow-88DF373B15998777955D8992088D5FCC', 'CDwindow-58F921927707F2FFBF4E368682D146B8']
brower.switch_to.window(brower.window_handles[1])        # 현재 브라우저를 다른 창으로 변경
brower.close()      # 현재 브라우저 종료

# print(brower.window_handles)        # 팝업 목록 확인, ['CDwindow-7B229C721CE208B718C5763AAF26C117', 'CDwindow-D28C1CCB1844B32094887ECD136D7A28']
brower.switch_to.window(brower.window_handles[1])        # 현재 브라우저를 다른 창으로 변경
brower.close()      # 이제 메인창만 남음
brower.switch_to.window(brower.window_handles[0])        # 현재 브라우저를 다른 창으로 변경

element = brower.find_element_by_css_selector('#txtGoEnd')
# brower.find_element_by_xpath('//*[@id="txtGoStart"]')
element.click()
element.send_keys(Keys.BACKSPACE)
element.send_keys(Keys.BACKSPACE)
element.send_keys('포항')
element.send_keys(Keys.ENTER)

element = brower.find_element_by_xpath('//*[@id="res_cont_tab01"]/form/div/fieldset/ul[2]/li[1]/a/img')       # xPath 방법으로 달력 객체 
element.click()

brower.switch_to.window(brower.window_handles[1])        # 달력 창으로 전환
element = brower.find_element_by_id('d20200815')
element.click()

brower.switch_to.window(brower.window_handles[0])        # 날짜 클릭과 동시에 달력창은 사라지지만 메인창으로 옮겨갔음을 지정해주야 함
element = brower.find_element_by_css_selector('#time > option:nth-child(13)')       # 시간 정함
element.click()

element = brower.find_element_by_css_selector('#res_cont_tab01 > form > div > fieldset > p > a > img')      # 예매 버튼 클릭
element.click()

