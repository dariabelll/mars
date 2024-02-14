from flask import Flask, render_template, redirect
from loginform import LoginForm
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/<name>')
@app.route('/index/<name>')
def index(name):
    return render_template('index.html', title=name)


@app.route('/training/<prof>')
def training(prof):
    return render_template('train.html', prof=prof)


@app.route('/list_prof/<listt>')
def prof(listt):
    proff = ["Инженер-исследователь",
             "Инженер-строитель",
             "Пилот",
             "Метеоролог",
             "Врач",
             "Экзобиолог"]
    return render_template('prof.html', listt=listt, proff=proff)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    with open("ans.json", "rt", encoding="utf8") as f:
        ans = json.loads(f.read())
    return render_template('auto_answer.html', ans=ans, title=ans['title'])


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
