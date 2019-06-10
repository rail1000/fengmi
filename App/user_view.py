from flask import app, Blueprint, url_for, render_template, Response, session, redirect
from flask import request

from App.goods_view import home
from App.user_model import user_model
from App.info_model import info



blue = Blueprint("user", __name__)





@blue.route('/register/', methods=['GET', 'POST'])
def register():
    return render_template('regst.html')


@blue.route('/regist/', methods=['GET', 'POST'])
def regist():
    error = None
    user = user_model()
    if request.method == 'GET':
        return render_template("regst.html")
    username = request.form.get('username')

    password = request.form.get('password1')
    repassword = request.form.get('password2')
    email = request.form.get('email')

    if request.method == "POST":
        if password == repassword:
            user = user_model()
            user_info = user.query_userAll_info(username)
            if user_info:
                error = '用户名重复，请重新输入！'
                return render_template("regst.html", error=error)
            else:
                user.regist(username, password, email)
                error = '注册成功！'
                return render_template('login.html', error=error)
        elif password != repassword:
            error = "密码不一致，请重新输入！"
            return render_template("regst.html", error=error)
    else:
        return render_template('regst.html', error=error)


@blue.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = user_model(username)
        rl_password = user.query_user_password(username)
        new = rl_password[0]
        if new['password'] == str(password):

            session['user'] = username

            return render_template('home.html')
        else:
            error = '密码或用户名错误，请重新输入！'
            return render_template('login.html', error=error)
    elif request.method == "GET":
        return render_template('login.html', error=error)


@blue.route('/usercenter/', methods=['GET', 'POST'])
def usercenter():
    username = session.get('user')
    user = user_model()
    user_content = info()
    # user_path = user.user_path(username)
    userAll_info = user.query_userAll_info(username)
    userAll_Done_display = user.query_userAll_display((userAll_info[0])['id'], 'done')
    userAll_undo_display = user.query_userAll_display((userAll_info[0])['id'], 'undo')
    userAll_display = user.query_userAll(username)

    chatRoom = user_content.query_TOuser(username)

    # if user_path:
    # user_path = "../static/user_head/200.png"

    return render_template('user_center.html', chatRoom=chatRoom, userAll_info=userAll_info,
                           userAll_Done_display=userAll_Done_display, userAll_undo_display=userAll_undo_display,
                           userAll_display=userAll_display)


@blue.route('/usercenter2/', methods=['GET', 'POST'])
def usercenter2():
    username = session.get('user')
    user = user_model()
    user_content = info()
    # user_path = user.user_path(username)
    userAll_info = user.query_userAll_info(username)
    userAll_Done_display = user.query_userAll_display((userAll_info[0])['id'], 'done')
    userAll_undo_display = user.query_userAll_display((userAll_info[0])['id'], 'undo')
    userAll_display = user.query_userAll(username)

    chatRoom = user_content.query_TOuser(username)

    # if user_path:
    # user_path = "../static/user_head/200.png"

    return render_template('usercen2.html', chatRoom=chatRoom, userAll_info=userAll_info,
                           userAll_Done_display=userAll_Done_display, userAll_undo_display=userAll_undo_display,
                           userAll_display=userAll_display)


@blue.route('/usercenter3/', methods=['GET', 'POST'])
def usercenter3():
    username = session.get('user')
    user = user_model()
    user_content = info()
    # user_path = user.user_path(username)
    userAll_info = user.query_userAll_info(username)
    userAll_Done_display = user.query_userAll_display((userAll_info[0])['id'], 'done')
    userAll_undo_display = user.query_userAll_display((userAll_info[0])['id'], 'undo')
    userAll_display = user.query_userAll(username)

    chatRoom = user_content.query_TOuser(username)

    # if user_path:
    # user_path = "../static/user_head/200.png"

    return render_template('usercen3.html', chatRoom=chatRoom, userAll_info=userAll_info,
                           userAll_Done_display=userAll_Done_display, userAll_undo_display=userAll_undo_display,
                           userAll_display=userAll_display)


@blue.route('/', methods=['GET', 'POST'])
def defaout():
    return render_template('login.html')


@blue.route('/temp/', methods=['GET', 'POST'])
def temp():
    return redirect(url_for('user.usercenter'))


@blue.route('/getpassword/', methods=['GET', 'POST'])
def get_password():
    error = None
    username = request.form['username']
    if username != '':
        user = user_model()
        send_psw = info()
        password = user.query_user_password(username)
        if password[0] != '':
            sender = 'rail1000@163.com'

            recipients = user.query_user_email(username)
            subject = '你好，这是一封系统自动发送的邮件！（请勿回复）'
            content = 'test'
            email = (recipients[0])['email']
            html = "<b>您的密码是" + (password[0])['password'] + "，请妥善保管</b>"
            import app
            app.send_mail(subject, sender, [email], content, html)
            error = '已发送邮件，请注意查收'
            return render_template('login.html', error=error)
        else:
            error = '请输入正确用户名！'
            return render_template('contact.html', error=error)
    else:
        error = '请输入正确内容！'
        return render_template('contact.html', error=error)


@blue.route('/contact/', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')


@blue.route('/home/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@blue.route('/qa/', methods=['GET', 'POST'])
def qa():
    return render_template('qa.html')


@blue.route('/add_infomation/', methods=['GET', 'POST'])
def add_infomation():
    return render_template('add_info.html')


@blue.route('/addsecond/', methods=['GET', 'POST'])
def add_second():
    return render_template('add_second.html')


@blue.route('/addtask/', methods=['GET', 'POST'])
def add_task():
    return render_template('add_task.html')


@blue.route('/importinfo/', methods=['GET', 'POST'])
def import_info():
    return render_template('important_info.html')


@blue.route('/add_wenjuan/', methods=['GET', 'POST'])
def add_wenjuan():
    return render_template('add_wenjuan.html')
