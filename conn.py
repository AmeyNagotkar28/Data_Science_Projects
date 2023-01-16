import pymysql
class Connection1:
    def getconnection(self):
        try:
            conn=pymysql.connect(host='localhost',user='root',password='',db='student_mangement')
        except Exception as e:
            print(e)
        else:
            print("Connection Successfull")
            return conn
