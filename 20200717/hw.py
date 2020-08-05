print('문제 1')
for i in range(1,101):
    print(i)

print('문제 2')
for j in range(1,6):
    for i in range(5):  
        print(j,end='')
    print()

print('문제 3')
for j in range(9,4,-1):
    for i in range(5):
        print(j,end='')
    print()

print('문제 4')
for j in (1,5):
    for i in range(j,j+4):
        print(i,end="")
    print()  

print('문제 5')
for i in range(1,10):
    print('8 *',i,'=',8*i)

print('문제 6')
for j in range(2,10):
    print(j,'단')
    for i in range(1,10):
        print(j,'*',i,'=',j*i)
    print()

print('문제 7')
for i in range(1,10):
    print('3 *',i,'=',3*i,end='   ')
print()

print('문제 8')
for j in range(1,6):
    for i in range(j):
        print(1,end='')
    print()

print('문제 9')
for i in range(1,101):    
    print('\t',i)

print('문제 10')
sum=0
l=list(range(1,101))
for i in range(100):
    sum=sum+l[i]
print(sum)

print('문제 11')
for i in range(1,6):
    print('*'*i,end='')
    print()

print('문제 12')
for j in range(1,6):
    for i in range(1,j+1):
        print(i,end='')
    print()

msg=''
for i in range(1,6):
    msg=msg+str(i)
    print(msg)

print('문제 13')
for j in range(2,10):
    for i in range(1,10):
        print(j,"*",i,'=',j*i,end="   ")
    print()

print('문제 14')
for i in range(5,0,-1):
    print('*'*i)

print('문제 15')
t=int(input("초 단위의 시간을 입력하시오"))
d=t//(60*60*24) # 1일=86,400초
h=(t%(60*60*24))//(60*60) # 1시간=3,600초
m=((t%(60*60*24))%(60*60))//60 # 1분=60초 -> t%(60*60)/60
s=((t%(60*60*24))%(60*60))%60 # -> t%60
print(d,'일',h,'시간',m,'분',s,'초 입니다.')

print('문제 15')
t=int(input("초 단위의 시간을 입력하시오"))
d=t//(60*60*24) # 1일=86,400초
h=(t%(60*60*24))//(60*60) # 1시간=3,600초
m=(t%(60*60))//60 # 1분=60초 -> t%(60*60)/60
s=t%60 # -> t%60
print(d,'일',h,'시간',m,'분',s,'초 입니다.')

print('문제 16')
m=int(input("입금액 얼마니"))
print('50000권 :',m//50000,'매')
print('10000권 :',(m%50000)//10000,'매')
print('5000권 :',((m%50000)%10000)//5000,'매')
print('1000권 :',(((m%50000)%10000)%5000)//1000,'매')
print('500권 :',((((m%50000)%10000)%5000)%1000)//500,'매')
print('100권 :',(((((m%50000)%10000)%5000)%1000)%500)//100,'매')
print('50권 :',((((((m%50000)%10000)%5000)%1000)%500)%100)//50,'매')
print('10권 :',(((((((m%50000)%10000)%5000)%1000)%500)%100)%50)//10,'매')
print('1권 :',(((((((m%50000)%10000)%5000)%1000)%500)%100)%50)%10,'매')

print('문제 16')
m=int(input("입금액 얼마니"))
print('50000권 :',m // 50000,'매')
print('10000권 :',(m % 50000) // 10000, '매')
print('5000권 :',(m % 10000) // 5000, '매')
print('1000권 :',(m % 5000) // 1000, '매')
print('500권 :',(m % 1000) // 500, '매')
print('100권 :',(m % 500) // 100, '매')
print('50권 :',(m % 100) // 50, '매')
print('10권 :',(m % 10), '매')


