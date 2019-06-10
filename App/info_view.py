from flask import app, Blueprint, url_for, render_template, Response, session, redirect
from flask import request
from App.info_model import info
from App.user_model import user_model


blue = Blueprint("info", __name__)


@blue.route('/addinfo<to_username>/', methods=['GET', 'POST'])
def add_info(to_username):
    user = user_model()
    username = session.get('user')
    content = request.form['info']
    tag = ''
    if tag == 'yes':
        sender = 'rail1000@163.com'
        recipients = [user.query_user_email(to_username)]
        subject = '你好，这是一封自动提醒邮件！（请勿回复）'
        html = "<b>" + content + "</b>"
        infomation = info()
        email = (recipients[0])['email']
        import app
        app.send_mail(subject, sender, [email], content, html)

        infomation.insert_info(username, to_username, content)

        return redirect(url_for('info.show_info'))

    else:
        infomation = info()
        infomation.insert_info(username, to_username, content)

        return redirect(url_for('info.show_info'))


@blue.route('/showinfo/', methods=['GET', 'POST'])
def show_info():
    infoma = info()
    username = session.get('user')
    user_content = info()


    chatRoom = user_content.query_TOuser(username)

    return render_template('chat.html', chatRoom=chatRoom)

@blue.route('/infobox<to_username>/', methods=['GET', 'POST'])
def infobox(to_username):
    infoma = info()
    username = session.get('user')
    user_content = info()
    infomation = infoma.query_info(username, to_username)

    chatRoom = user_content.query_TOuser(username)

    return render_template('chats.html', infomation=infomation,chatRoom=chatRoom,to_username=to_username)


@blue.route('/info_ent/', methods=['GET', 'POST'])
def info_ent():

    to_username = request.form['to_username']
    return redirect(url_for('info.infobox', to_username=to_username))





