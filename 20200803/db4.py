import cx_Oracle

# 1. conneciton 객체 생성
connection = cx_Oracle.connect('scott','tigertiger','orcl.c2yvx9kfplxi.ap-northeast-2.rds.amazonaws.com:1521/orcl')
print(connection)
# 2.cursor 객체
cur = connection.cursor()
# 3. 사용할 sql문 객체
sql = '''
insert into dept values(:deptno,:dname,:loc)
'''
sql2 = '''
insert into dept(deptno, loc) values(:deptno, :loc) 
''' # NULL의 암시적 삽입법 :컬럼을 지정하여 값을 삽입
# 4. 실행
# cur.execute(sql,[1,'SALESMAN','SEOUL']) 
# cur.execute(sql,[2,None,'BUSAN']) # NULL의 명시적 삽입법
cur.execute(sql2,[3,'INCHEON'])
connection.commit()
# 5. 로직처리

# 6. 자원 반납
connection.close()