# lottosalary라는 모듈에 raise_rnd_salary, reduce_rnd_salary라는 함수 정의해놓음
import salary
import random
def raise_rnd_salary(sal): # 50% 확율로 급여가 50% 인상
    rnd=random.randint(0,1)
    if rnd==0:
        print('강화성공!!')
        return sal*1.5
    else:
        return sal    

    
def reduce_rnd_salary(sal): # 50% 확율로 급여가 20% 감소    
    rnd=random.randint(0,1)
    if rnd==0:
        return salary.reduce_sal(sal)
    else:
        return sal    


if __name__ == '__main__': # 이름이 메인일 때만 실행하는 조건 ->다른 파일에서는 
    print(raise_rnd_salary(2000))
    print(reduce_rnd_salary(2000))