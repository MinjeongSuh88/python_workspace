# 가위 바위 보
import random
print('1. 가위    2. 바위    3. 보')
userInput = int(input('가위, 바위, 보 중 선택하세요'))
userInput -= 1 # 사용자로부터 입력 받은 값을 인덱스에 맞게 0부터로 바꿈

li=['가위','바위','보'] # 가위, 바위, 보가 들어있는 리스트 만듦
idx=random.randint(0,2) # 0과 2사이의 랜덤 정수 생성
# print(idx, li[idx])

print('사용자 입력값 :',userInput+1, li[userInput]) # 승부 판정을 사용자의 입력값과 컴퓨터의 랜덤값의 차를 비교
print('컴퓨터 랜덤값 :',idx+1, li[idx]) # 승부 판정을 사용자의 입력값과 컴퓨터의 랜덤값의 차를 비교

if userInput-idx == 0: # 차이값이 0이면 비김
    print('비김')
elif userInput-idx == -2 or userInput-idx == 1: # 1이거나 -2이면 사용자 승
    print('승!!') 
elif userInput-idx == -1 or userInput-idx == 2: # -1이거나 2이면 컴퓨터 승
    print('졌지롱 메롱')

