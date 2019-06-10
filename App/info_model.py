import pymysql
from flask_mail import Message,Mail


class info:

    def __init__(self, username='', to_username='', infomation='', up_data='', ):
        self.username = username
        self.to_username = to_username
        self.infomation = infomation
        self.up_data = up_data


    def insert_info(self,username,to_username,infomation):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='com.fengmi')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # print(self.username)
        sql = "insert into content(id,username,to_username,info,up_data)VALUES(0,\'"+username+"\',\'"+to_username+"\',\'"+infomation+"\',(SELECT NOW()))"

        cursor.execute(sql)
        cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()

    def query_info(self, username, to_username):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='com.fengmi')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # print(self.username)
        sql = "select * from (select * from content where username=\'" + username + "\' OR to_username=\'" + username + "\') as temp where temp.username=\'" + to_username + "\' or temp.to_username=\'" + to_username + "\'"

        cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()

        return res


    def query_TOuser(self,username):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='com.fengmi')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # print(self.username)
        sql = "select * from content where username=\'"+username+"\' GROUP BY to_username"

        cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return res

    def query_tagdo(self,goods_id):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='com.fengmi')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # print(self.username)
        sql = "select tag from tagdo where goods_id="+goods_id

        cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return res



