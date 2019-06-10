import os

from flask import app, Blueprint, url_for, render_template, Response, session, redirect
from flask import request
from App.goods_model import goods
from App.user_model import user_model

blue = Blueprint("goods", __name__)


@blue.route('/home/', methods=['GET', 'POST'])
def home():
    username = session.get('user')
    user = user_model()
    user_path = user.user_path(username)

    return render_template('home.html', user_path=user_path)


@blue.route('/post_info_tans<parm>/', methods=['GET', 'POST'])
def post_info_tans(parm):
    username = session.get('user')
    user = user_model()
    # user_path = user.user_path(username)

    good = goods()
    tag_goods = good.query_all_goods(parm)

    return render_template('info_tans.html', tag_goods=tag_goods)


@blue.route('/post_second<parm>/', methods=['GET', 'POST'])
def post_second(parm):
    username = session.get('user')
    user = user_model()
    # user_path = user.user_path(username)

    good = goods()
    tag_goods = good.query_all_goods(parm)

    return render_template('second.html', tag_goods=tag_goods)


@blue.route('/post_task<parm>/', methods=['GET', 'POST'])
def post_task(parm):
    username = session.get('user')
    user = user_model()
    # user_path = user.user_path(username)

    good = goods()
    tag_goods = good.query_all_goods(parm)

    return render_template('task.html', tag_goods=tag_goods)


@blue.route('/post_task1<parm>/', methods=['GET', 'POST'])
def post_task1(parm):
    username = session.get('user')
    user = user_model()
    # user_path = user.user_path(username)

    good = goods()
    tag_goods = good.query_all_goods(parm)

    return render_template('post_task.html', tag_goods=tag_goods)


@blue.route('/post_wenjuan<parm>/', methods=['GET', 'POST'])
def post_wenjuan(parm):
    username = session.get('user')
    user = user_model()
    # user_path = user.user_path(username)

    good = goods()
    tag_goods = good.query_all_goods(parm)

    return render_template('wenjuan.html', tag_goods=tag_goods)


@blue.route('/addTask<parm>/', methods=['GET', 'POST'])
def add_task(parm):
    error = None
    good = goods()
    username = session.get('user')
    family = parm
    title = request.form['title']
    descrip = request.form['descrip']
    money = '0'
    # people = int(request.form['people'])

    close_date = request.form['close_date']
    photo_path = ''

    good.add_goods(family, username, title, descrip, money, close_date, photo_path)
    error = '添加成功！'
    return render_template('add_task.html', error=error)


@blue.route('/addsec<parm>/', methods=['GET', 'POST'])
def add_second(parm):
    error = None
    good = goods()
    username = session.get('user')
    family = parm
    title = request.form['title']
    descrip = request.form['descrip']
    money = request.form['money']
    # people = int(request.form['people'])

    close_date = '2099/12/31'
    basedir = os.path.abspath(os.path.dirname(__file__))
    photo = request.files['photo']

    path = basedir + "/goods_pic/"
    file_path = path + photo.filename

    photo.save(file_path)

    photo_path = "/static/goods_pic/" + photo.filename
    good.add_goods(family, username, title, descrip, money, close_date, photo_path)
    error = '添加成功！'
    return render_template('add_second.html', error=error)


@blue.route('/addinfo_trans<parm>/', methods=['GET', 'POST'])
def add_info(parm):
    error = None
    good = goods()
    username = session.get('user')
    family = parm
    title = request.form['title']
    descrip = request.form['descrip']
    money = '0'
    # people = int(request.form['people'])

    close_date = request.form['close_date']
    photo_path = ''

    good.add_goods(family, username, title, descrip, money, close_date, photo_path)
    error = '添加成功！'
    return render_template('add_info.html', error=error)


@blue.route('/addwenjuan/', methods=['GET', 'POST'])
def add_wenjuan():
    usr = user_model()
    good = goods()
    username = session.get('user')
    family = 'wenjuan'
    title = request.form['title']
    descrip = request.form['descrip']
    money = request.form['money']

    close_date = request.form['close_date']
    people = request.form['people']

    error = None
    usr = user_model()
    temp = usr.query_userAll_info(username)
    user_money = int((temp[0])['money'])

    num = int(people)

    if user_money < int(money) * num:
        error = '余额不足，无法发布！'
        return render_template('add_wenjuan.html', error=error)
    else:
        good.add_goods(family, username, title, descrip, money, close_date, people)
        usr.update_money(username, str(user_money - int(money) * num))
        error = '添加成功'
        return render_template('add_wenjuan.html', error=error)


@blue.route('/query<id>/', methods=['GET', 'POST'])
def query(id):
    good = goods()
    tag_goods = good.query_goodsByid(id)

    return render_template('post_second.html', tag_goods=tag_goods)


@blue.route('/all_like/', methods=['GET', 'POST'])
def all_like():
    st = request.form['str']
    good = goods()

    all_goods = good.query_goodsBystr(st)

    return render_template('search_result.html', all_goods=all_goods)
