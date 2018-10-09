from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap
import pymysql


db = pymysql.connect(host='localhost', user='root', password='hi', db='contact_list_db')
cur = db.cursor()

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = "miv140130"

class SearchForm(FlaskForm):
    search = StringField('Search', validators=[InputRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    s_form = SearchForm()
    cur.execute("SELECT * FROM contact;")
    data = list(cur)
    field_names = [i[0] for i in cur.description]
    length = len(data[0])
    return render_template('index2.html', data=data, field_names=field_names, length=length)

@app.route('/form')
def form():
    cur.execute("SELECT * FROM contact WHERE FName='Hogan';")
    data = cur.fetchall()
    return render_template('form.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

    