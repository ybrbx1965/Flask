from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from flask import redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import send_from_directory

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
            f = open('lp.txt','r')
            lp = f.read().split('\n')
            for i in lp:
                if i != '':
                    i = i.split()
                    if request.form['username'] == i[0] and request.form['password'] == i[1]:
                        return redirect('/main')
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/main', methods=['GET', 'POST'])
def site():
    if request.method == "GET":
        return render_template('site1.html')

@app.route('/photogallery', methods=['GET', 'POST'])
def pg():
    if request.method == "GET":
        return render_template('photogallery.html')


@app.route('/register', methods=['GET', 'POST'])
def reg():
    if request.method == "GET":
        return render_template('register.html')
    if request.method == "POST":
        f = open('lp.txt', 'a')
        f.write('\n')
        st = str(request.form['email']) +' '+ str(request.form['password']) +' '+ str(request.form['telephone'])
        f.write(st)
        f.close()
    return redirect('/main')


@app.route('/sotrud', methods=['GET', 'POST'])
def sot():
    if request.method == "GET":
        return render_template('sotrud.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port='8000', debug=True)
