import time

def saveLog(savedir,money,balance,mode):
    if mode: # mode라는 매개변수에 True가 대체되어 -> '만약에 참이면'이라는 뜻
        type ='출금'
    else: # 참이 아니면
        type = '입금'
    with open(savedir,'a',encoding='utf-8') as file: # 현재 디렉토리에 bank.log 파일을 생성
        file.write('현재 시간 :'+time.ctime()+', '+type+'액 :'+str(money)+', 현재잔액 :'+str(balance)+'\n') # 현재 시간, 출금액, 현재 잔액 저장