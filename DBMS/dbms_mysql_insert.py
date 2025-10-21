# dbms_mysql_select.py
import pymysql
# 서버 재시작: restart;

# MySQL 서버에 연결
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="exampledb"
)
# 커서 생성 => 명령어 작성
cursor = conn.cursor()

# 명령어 실행
sql1 = """
INSERT INTO employees(id,name,DeptID,ManagerID) 
VALUES(8,'kenneth',8,101);
"""

sql1 = """
INSERT INTO employees(id,name,DeptID,ManagerID) 
VALUES(%s,%s,%s,%s);
"""
cursor.execute(sql1, (8,'kenneth',8,101))
conn.commit()
print("데이터 삽입 완료")
# 연결 해제
conn.close()