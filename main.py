import flask
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'help me'


@app.route('/')
def wellcome_view():
    return flask.render_template('wellcome.html')


@app.route('/register/', methods=['GET', 'POST'])
def register_view():
    form = RegisterForm()

    if flask.request.method == "GET":
        return flask.render_template('register.html', form=form)

    return '<div class="row featurette">' \
           '<div class="col-md-7 order-md-2">' \
           '<h2 class="featurette-heading fw-normal lh-1">Поздравляю {} {}. Вы Получили Бесплатно КАПИБАРУ!!!</h2>' \
           '<p class="lead">Теперь Ваша Жизнь наладится, впервые, я прав? Кто бы что не говорил,' \
           ' но Завидовать они будут с полна. Гордитесь им и не давайте в обиду.</p>' \
           '</div>' \
           '<div class="col-md-5 order-md-1">' \
           '<p><img width="500" height="500" ' \
           'src = "https://avatars.dzeninfra.ru/get-zen_doc/3655132/pub_606c66bc6b07e37898825722_' \
           '606c66d16d52a37dda83faa9/scale_1200"></p>' \
           '</div>' \
           '</div>'.format(form.second_name.data, form.name.data)


class RegisterForm(FlaskForm):
    name = StringField('Имя: ')
    second_name = StringField('Фамилия: ')
    submit = SubmitField('Отправить')


if __name__ == '__main__':
    app.run(debug=True)
