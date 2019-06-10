import pymysql

class goods:

    def __init__(self, username='', family='', title='', decsrip='', money='',up_date='',close_date='',photo_path=''):
        self.username = username
        self.family = family
        self.title = title
        self.decsrip = decsrip
        self.money = money
        self.up_date = up_date
        self.close_date = close_date
        self.photo_path = photo_path

    def query_all_goods(self,family):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='com.fengmi')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "select * from goods where family=\'"+family+"\' and status=0"

        cursor.execute(sql)
        res = cursor.fetchall()
        print(res)
        conn.commit()
        cursor.close()
        conn.close()
        return res

    def add_goods(self,family,username,title,descrip,money,close_date,photo_path):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='com.fengmi')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # print(self.username)
        if close_date is  not '':
            if close_date is not None:
                sql = "insert into goods(id,family,username,title,descrip,money,up_date,close_date,photo_path,status)VALUES(0,\'"+family+"\',\'"+username+"\',\'"+title+"\',\'"+descrip+"\',\'"+money+"\',(SELECT NOW()),\'"+close_date+"\',\'"+photo_path+"\',0)"
        if close_date is '' or None:
            close_date = 0
            sql = "insert into goods(id,family,username,title,descrip,money,up_date,close_date,photo_path,status)VALUES(0,\'" + family + "\',\'" + username + "\',\'" + title + "\',\'" + descrip + "\',\'" + money + "\',(SELECT NOW()),\'" + close_date + "\',\'" + photo_path + "\',0)"

        cursor.execute(sql)
        #res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()


    def query_money(self,goods_id):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='com.fengmi')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # print(self.username)
        sql = "select money from goods where id=\'"+goods_id+"\'"

        cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return res

    def query_user(self,goods_id):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='com.fengmi')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # print(self.username)
        sql = "select username from goods where id=\'"+goods_id+"\'"

        cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return res

    def add_wenjuan(self,family,username,title,descrip,money,close_date,people):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='com.fengmi')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # print(self.username)
        if close_date is  not '':
            if close_date is not None:
                sql = "insert into goods(id,family,username,title,descrip,money,up_date,close_date,people,status)VALUES(0,\'"+family+"\',\'"+username+"\',\'"+title+"\',\'"+descrip+"\',\'"+money+"\',(SELECT NOW()),\'"+close_date+"\',\'"+people+"\',0)"
        if close_date is '' or None:
            close_date = 0
            sql = "insert into goods(id,family,username,title,descrip,money,up_date,close_date,people,status)VALUES(0,\'" + family + "\',\'" + username + "\',\'" + title + "\',\'" + descrip + "\',\'" + money + "\',(SELECT NOW()),\'" + close_date + "\',\'" + people + "\',0)"

        cursor.execute(sql)
        #res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()

    def do_qingqiu(self,goods_id):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='com.fengmi')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # print(self.username)
        sql = "update tagdo set tag='done' where goods_id=\'"+goods_id+"\'"

        cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return res

    def query_goodsByid(self,id):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='com.fengmi')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "select * from goods where id=\'"+id+"\' and status=0"

        cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return res

    def query_goodsBystr(self, st):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='com.fengmi')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "select * from goods where title like '%"+st+"%'"

        cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return res




