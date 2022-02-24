import flask


app = flask.Flask(__name__)


@app.route('/')
@app.route('/index/<t>')
def index(t):
    user = "Ученик Яндекс.Лицея"
    return flask.render_template('base.html', title=t, username=user)
