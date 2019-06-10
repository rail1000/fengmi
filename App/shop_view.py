from flask import app, Blueprint, url_for, render_template, Response, session, redirect, flash
from flask import request
from App.user_model import user_model
from App.goods_model import goods
from App.info_model import info
from App.user_view import usercenter


blue = Blueprint("shop", __name__)


@blue.route('/shoping<tag>/', methods=['GET', 'POST'])
def shoping(tag):
    error=None
    infoma = info()
    if tag == 'task':

        error = None
        username = session.get('user')

        goods_id = request.form['goods_id']
        good = goods()

        to_username = good.query_goodsByid(goods_id)

        user = user_model()

        sender = 'rail1000@163.com'
        recipients = user.query_user_email(username)
        email_temp = user.query_user_email((to_username[0])['username'])
        email = (email_temp[0])['email']
        subject = '你好，这是一封自动提醒邮件！（请勿回复）'
        to_email = (recipients[0])['email']
        content = '注意，您的一份订单已被用户' + email + '关注，请及时联系对方！'
        html = "<b>" + content + "</b>"
        import app
        app.send_mail(subject, sender, [to_email], content, html)
        error = '已成功向对方发送提醒邮件，请及时与对方联系！'
        return render_template('user_center.html',error=error)
        '''
        username = session.get('user')
        goods_id = request.form['goods_id']
        usr = user_model()
        good = goods()
        temp = usr.query_userAll_info(username)
        temp1 = good.query_money(goods_id)
        temp2 = good.query_user(goods_id)
        user_money = int((temp[0])['money'])
        goods_money = int((temp1[0])['money'])
        goods_user = str((temp2[0])['username'])
        id = int(goods_id)
        do =infoma.query_tagdo(id)

        do_tag = (do[0])['tag']
        if do_tag == 'done':
            error = '已成功向对方发送完成提醒邮件，请及时与对方联系！'
            money=user_money
            usr.update_money(username, money)

            return redirect(url_for('user.usercener',error=error))
        else:
            error='订单还未完成，请尽快完成'
            return redirect(url_for('user.usercener',error=error))
        '''
    elif tag == 'wenjuan':





        '''
        error = None
        username = session.get('user')
        goods_id = request.form['goods_id']
        usr = user_model()
        good = goods()
        temp = usr.query_userAll_info(username)
        temp1 = good.query_money(goods_id)
        temp2 = good.query_user(goods_id)
        user_money = int((temp[0])['money'])
        goods_money = int((temp1[0])['money'])
        goods_user = str((temp2[0])['username'])
        temp3 = usr.query_userAll_info(goods_user)
        goods_user_money = int((temp3[0])['money'])

        if user_money < goods_money:
            error = '错误，你的余额不足！'
            return render_template('', error=error)
        else:
            money = user_money - goods_money
            goods_user_money = goods_user_money + goods_money
            usr.update_money(username, money)
            usr.update_money(goods_user, goods_user_money)

            return redirect(url_for('user.usercenter', error=error))
        '''

    elif tag == 'second':
        error = None
        username = session.get('user')

        goods_id = request.form['goods_id']
        good = goods()

        to_username = good.query_goodsByid(goods_id)

        user = user_model()

        sender = 'rail1000@163.com'
        recipients = user.query_user_email(username)
        email_temp = user.query_user_email((to_username[0])['username'])
        email = (email_temp[0])['email']
        subject = '你好，这是一封自动提醒邮件！（请勿回复）'
        to_email = (recipients[0])['email']
        content = '注意，您的一份商品已被用户' + email + '关注，请及时联系对方！'
        html = "<b>" + content + "</b>"
        import app
        app.send_mail(subject, sender, [to_email], content, html)
        error = '已成功向对方发送提醒邮件，请及时与对方联系！'
        return render_template('user_center.html',error=error)


        '''
        error = None
        username = session.get('user')
        goods_id = request.form['goods_id']
        usr = user_model()
        good = goods()
        temp = usr.query_userAll_info(username)
        temp1 = good.query_money(goods_id)
        temp2 = good.query_user(goods_id)
        user_money = int((temp[0])['money'])
        goods_money = int((temp1[0])['money'])
        goods_user = str((temp2[0])['username'])
        temp3 = usr.query_userAll_info(goods_user)
        goods_user_money = int((temp3[0])['money'])

        if user_money < goods_money:
            error = '错误，你的余额不足！'
            return render_template('', error=error)
        else:
            money = user_money - goods_money
            goods_user_money = goods_user_money + goods_money
            usr.update_money(username, money)
            usr.update_money(goods_user, goods_user_money)

            return redirect(url_for('user.usercenter', error=error))
            '''






@blue.route('/do_qingqiu<parm>/', methods=['GET', 'POST'])
def do_qingqiu(parm):
    error = None
    good = goods()
    error = '已确认完成订单'
    good.do_qingqiu(parm)

    return render_template('user_center.html', error=error)


@blue.route('/qingqiu<parm>/', methods=['GET', 'POST'])
def qingqiu(parm):
    username = parm
    user = user_model()
    sender = 'rail1000@163.com'
    recipients = user.query_user_email(username)
    subject = '你好，这是一封自动提醒邮件！（请勿回复）'
    content = '您已有一份订单被完成,请登陆确认' + +''
    html = "<b>" + content + "</b>"
    print(recipients)
    email = (recipients[0])['email']
    app.send_mail(subject, sender, [email], content, html)

    return redirect(url_for('user.usercenter'))


@blue.route('/make_qingqiu<parm>/', methods=['GET', 'POST'])
def make_qingqiu(parm):


    pass
