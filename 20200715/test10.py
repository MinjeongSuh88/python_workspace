# csv파일

a,b,c=input("숫자 3개를 콤마로 구분해서 입력하세요 : ").split(",") # 입력 받은 문자열을 ,로 구분
print("a :",a,", b :",b,", c :",c) 

# print 함수에는 자동 엔터 기능이 들어가 있음
print(100,200,300,sep=", ") # 프린트할 값의 구분을 ,로 함
print(100,200,300) # ,는 프린트할 값을 나열하여 출력하는데 사이에 스페이스가 한 칸 들어감
print("Hello","Pyhon","World") 
print("Hello","Pyhon","World",sep=" ") #프린트할 값의 구분을 스페이스 한 칸으로 함
print("Hello","Pyhon","World",sep="\n") # 특수문자  제어문자 :엔터-\n, 탭-\t
print("아\n날씨가\n좋다.\n놀\t러\t가\t야\t지.... ㅠㅠ") 

print("오늘은") # 프린터에는 원래 끝에 자동 엔터 기능이 있음
print("수요일")
print("내일은")
print("목요일")

print("오늘은",end="\t") # 프린트의 끝을 탭 기능으로 바꿈
print("수요일",end=",\t")
print("내일은",end="\t")
print("목요일")

year,month,day,hour,minute,second=2020,7,15,18,"00","00" # 변수 6개에 값을 할당
print("오늘은",end=" ") # 프린트의 끝을 스페이스 한 칸으로 함
print(year,month,day,sep="/",end=" ") # 프린트할 값의 구분을 /로 하고 프린트의 끝은 스페이스 한 칸으로 함
print(hour,minute,second,sep=":",end="  ") # 프린트할 값의 구분을 :로 하고 프린트의 끝은 스페이스 한 칸으로 
print("입니다.")
print(year,month,day,sep="/",end=" ")
print(hour,minute,second,sep=":")