import cx_Oracle
# 1. conneciton 객체 생성
connection = cx_Oracle.connect('scott','tigertiger','   :1521/orcl')
print(connection)

# 2.cursor 객체
cur = connection.cursor()

# 3. 사용할 sql문 객체
sql = '''
select empno, ename, sal
from emp 
where ename = :txt 
''' # 바이드 변수? 앞에는 콜론을 붙여줌

# 4. 실행
cur.execute(sql,txt='SCOTT') # 매개변수 자리에 SCOTT값이 전달 됨
print(cur)

# 5. 로직처리
for empno,ename,sal in cur:
    # print('%d \t %s \t %d'%empno,ename,sal) ?
    print('{} \t {} \t {}'.format(empno,ename,sal))

# 6. 자원 반납
connection.close()
