import flask


app = flask.Flask(__name__)


@app.route('/<t>')
@app.route('/index/<t>')
def index(t):
    user = "Ученик Яндекс.Лицея"
    return flask.render_template('base.html', title=t, username=user)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')