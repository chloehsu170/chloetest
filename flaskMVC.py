#-*-coding:utf-8-*- 
__author__ = 'chloe'
from flask import Flask,request,render_template

app = Flask(__name__)
@app.route('/', methods =['GET','POST'])
def home():
    return render_template('home.html')
@app.route('/signin',methods =['GET'])
def signin_form():
    return render_template('form.html')
@app.route('/signin',methods =['POST'])
def sign():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin_ok.html',username = username)
    return render_template('form.html',message = 'bad username or password!',username = username)

if __name__ == '__main__':
    app.run()