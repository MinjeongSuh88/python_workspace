with open('./20200727/rain.txt','r',encoding='utf-8') as file: # 유니콘 8로 되어있는 타입의 파일을 불러와
    data = file.read()
    print(data)

lines = ['안녕하세요\n','오늘은 금요일\n','이면 좋겠네요\n']    

with open('./20200727/msg2.txt','w',encoding='utf-8') as file: # 유니콘 8로 되어있는 타입의 파일을 작성
    file.writelines(lines)  # 문자열로만 구성되어있는 배열 단위로 한 줄 쓰기

with open('./20200727/msg2.txt','r',encoding='utf-8') as file: # 유니콘 8로 되어있는 타입의 파일을 불러와
    data = file.readlines() # 한 줄 읽기
    print(data)