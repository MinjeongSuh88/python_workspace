'''3번 스텝인 .close()를 안 해도 되는 명령어
with open('파일명','파일모드') as 파일객체: 
    코드
'''
# with open('./20200727/msg.txt','w') as file: -> 해당 디렉토리에서 연 파일을 file이라는 이름의 객체에 넣음
#     file.write('오늘은 여기까지...\n')
with open('./20200727/msg.txt','r') as file: # 
    print(len([i for i in file.read().split() if i == '에이수스']))
# unicode :전세계의 문자를 단일코드로 만듦
 