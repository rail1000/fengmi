import pymysql


class user_model():

    def __init__(self, username='', password='', sex='', figure_path='', phone='', email=''):
        self.username = username
        self.password = password
        self.sex = sex
        self.figure_path = figure_path
        self.phone = phone

    def regist(self, username, password, email):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='com.fengmi')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # print(self.username)
        sql = "insert into usr(id,username,password,email)VALUES(0,\'" + username + "\',\'" + password + "\',\'" + email + "\')"

        cursor.execute(sql)
        # res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()

    def query_user_password(self, username):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='com.fengmi')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # print(self.username)
        sql = "select password from usr where username=\'" + username + "\'"

        cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return res

    def query_userAll_info(self, username):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='com.fengmi')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # print(self.username)
        sql = "select * from usr where username=\'" + username + "\'"

        cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return res

    def query_userAll_display(self, user_id, tag):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='com.fengmi')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # print(self.username)
        sql = "SELECT * from (tagdo,goods) where tagdo.goods_id=goods.id and tagdo.tag=\'" + tag + "\' and tagdo.user_id=\'" + str(user_id) + "\'"

        cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return res

    def query_userAll(self, username):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='com.fengmi')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # print(self.username)
        sql = "SELECT * from goods where username=\'" + username + "\'"

        cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return res

    # 查询用户头像
    '''
    def user_path(self, username):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='com.fengmi')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # print(self.username)
        sql = "SELECT figure_path from goods where username=\'" + username + "\'"

        cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return res
    '''
    def query_user_email(self, username):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='com.fengmi')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # print(self.username)
        sql = "select email from usr where username=\'" + username + "\'"

        cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return res

    def update_money(self, username, money):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='com.fengmi')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # print(self.username)
        sql = "update usr set money=" + money + " where username=\'" + username + "\'"

        cursor.execute(sql)
        # res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()

    def insert_tagdo(self, user_id, goods_id):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='com.fengmi')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # print(self.username)
        sql = "insert into tagdo(id,user_id,goods_id,tag)VALUES(0,"+user_id+","+goods_id+",'done')"

        cursor.execute(sql)
        # res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()


