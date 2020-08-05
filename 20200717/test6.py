# 제어문
# 조건 분기문
# 주어진 조건 발생하면 다른 문장이 실행되게 처리
# if 조건:
#     처리할 문장
# elif 조건: 
#     처리할 문장
# else 조건: # else는 조건이 있어도 되고 없어도 됨
#     처리할 문장

# score=int(input("당신의 성적을 입력하시오"))
# print(score>90)
# if score>=90: # 조건을 만족하는지 
#     print("당신의 성적은",score,"입니다. A 학점")
#     print("축하합니다. 짝짝짝!!")    
# elif score>=80: # 위의 조건을 만족하지 않으면 이 조건으로 내려옴
#     print("당신의 성적은",score,"입니다. B 학점")    
# elif score>=70: # 위의 조건을 만족하지 않으면 이 조건으로 내려옴
#     print("당신의 성적은",score,"입니다. C 학점")    
# elif score>=60: # 위의 조건을 만족하지 않으면 이 조건으로 내려옴
#     print("당신의 성적은",score,"입니다. D 학점")    
# else :
#     print("Fail")


print("문제 1")
for i in range(1,21):
    print(i)
for i in range(1,21):
    if i%2 != 0:
        print(i)
print("문제 2")
for i in range(1,10):
    if i%2 != 0:
        print("5 *",i,"=",5*i)
    else :
        print("5 *",i,"=",'****')
   
