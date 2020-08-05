# set 내부 표현식도 가능
keyword = '오늘은 비가 언제 까지 올까요?'.split() # keyword는 리스트로 지정됨
print(keyword, type(keyword)) 

print({len(word) for word in keyword}, type({len(word) for word in keyword})) # 리스트 요소들의 길이를 셋으로 지정
print({len(word) for word in keyword if len(word)>3}) # 문자열 길이가 3보다 큰 워드만


# Dictionary Comprehension 내부 표현식도 가능
countrys = {'한국':'서울','일본':'도쿄','중국':'북경','UAE':'아부다비'} # 키:밸류
capital = {country:capital for country,capital in countrys.items()} # for문에 차례대로 키, 밸류 값으로 country, capital 변수에 각각 지정 됨
print(capital)
print({key for key in countrys}) 