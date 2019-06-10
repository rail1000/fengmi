import os

from flask import Flask, render_template, session, redirect, url_for, request, Blueprint
from App.user_view import blue
from App.goods_view import blue as blue1
from App.info_view import blue as blue2
from App.shop_view import blue as blue3
import json
from flask_mail import Mail,Message



app = Flask(__name__)


app.register_blueprint(blueprint=blue)
app.register_blueprint(blueprint=blue1)
app.register_blueprint(blueprint=blue2)
app.register_blueprint(blueprint=blue3)


app.config['SECRET_KEY'] = '123'
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'rail1000@163.com'
app.config['MAIL_PASSWORD'] = 'SMTP19980718'

mail = Mail(app)
def send_mail( subject, sender, recipients, text_body, html_body):

    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body

    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)