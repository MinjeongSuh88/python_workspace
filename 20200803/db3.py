import cx_Oracle

connection = cx_Oracle.connect('scott','tigertiger','orcl.c2yvx9kfplxi.ap-northeast-2.rds.amazonaws.com:1521/orcl')
# print(connection)

cur = connection.cursor()

sql = '''
select empno,ename,job,deptno
from emp
where deptno = :txt
'''

cur.execute(sql,txt=10)
print(cur)

for empno,ename,job,detpno in cur:
    print('{} \t {} \t {} \t {}'.format(empno,ename,job,detpno)) # 괄호 안에는 숫자 또는 빈칸 없이

connection.close()