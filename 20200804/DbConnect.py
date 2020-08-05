import cx_Oracle

class DbConnect:
    def __init__(self, host, dbname, user, password, port=1521):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.dbname = dbname
        self.connection = cx_Oracle.connect(self.user, self.password, self.host+':'+self.port+'/'+self.dbname)
        print(self.connection)

    def execute(self, sql):
        self.sql = sql # sql 객체 생성
        cur = self.connection.cursor() # cursor 객체 생성
        cur.execute(sql) # 커서로 sql문을 실행
        resultList = [] # 빈 리스트 생성
        for x in cur:
            resultList.append(x) # 커서가 실행해온 값을 리스트에 추가
        return resultList # 완성된 리스트들 리턴값으로 
        self.connection.close() # 연결 종료

if __name__ == "__main__":
    db = DbConnect('192.168.0.68','orcl','scott','tiger','1521')        
    print(db.execute('select * from dept'))