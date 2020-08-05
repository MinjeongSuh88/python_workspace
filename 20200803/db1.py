# DB에 연결하기
import cx_Oracle

# print(cx_Oracle.init_oracle_client())
# conneciton = cx_Oracle.connect('id','pw','서버ip:1521/db명') # 데이터베이스에 컨넥션이라는 것을 만들어야 함
connection = cx_Oracle.connect('scott','tigertiger','orcl.c2yvx9kfplxi.ap-northeast-2.rds.amazonaws.com:1521/orcl') # 데이터베이스에 컨넥션이라는 것을 만들어야 함
# 서버 ip : orcl.c2yvx9kfplxi.ap-northeast-2.rds.amazonaws.com    
print(connection)

cur = connection.cursor() # 커서 객체 만듦
query = 'select * from dept' # 사용할 sql 준비
cur.execute(query) # 커서를 통해서 이 문장 실행
for x  in cur:
    print(x) # 결과는 튜플 형식

# 연결 끊기
connection.close() # db는 대기 중이기 때문에 자원 소모됨        

