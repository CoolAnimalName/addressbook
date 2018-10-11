from flask import Flask, render_template, flash, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DateField
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
    submit = SubmitField('Submit')

class EntryForm(FlaskForm):
    fname = StringField('First Name ', validators=[InputRequired()])
    mname = StringField('Middle Name ')
    lname = StringField('Last Name ', validators=[InputRequired()])
    haddress = StringField('Home address ')
    hcity = StringField('Home city ')
    hstate = StringField('Home state ')
    hzip = StringField('Home zip ')
    waddress = StringField('Work address ')
    wcity = StringField('Work city ')
    wstate = StringField('Work state ')
    wzip = StringField('Work zip ')
    cnum = StringField('Cell Phone number ')
    careacode = StringField('Cell Phone area code ')
    hnum = StringField('Home Phone number ')
    hareacode = StringField('Home Phone area code ')
    wnum = StringField('Work Phone num ')
    wareacode = StringField('Work Phone area code ')
    dtype = SelectField(u'Type of Date: ',
                        choices=[('birthdate', 'Birthday'), 
                                ('anniversary', 'Anniversary'), 
                                ('other', 'Other')])
    date = DateField('Date')
    submit = SubmitField('Submit')

class DeleteEntry(FlaskForm):
    delete = SubmitField('Delete')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        session['search'] = form.search.data
    cur.execute("SELECT * FROM contact;")
    data = cur.fetchall()
    field_names = [i[0] for i in cur.description]
    length = len(data[0])
    return render_template('index.html', data=data, field_names=field_names, length=length, form=form)

@app.route('/newform', methods=['GET', 'POST'])
def newform():
    form = EntryForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
        #display an alert that
    else:
        flash('Please fill out First Name and Last Name Fields')
    return render_template('newform.html', form=form)

@app.route('/edit/<contact_id>')
def edit(contact_id):
    return render_template('edit.html', contact_id=contact_id)

@app.route('/delete/<contact_id>')
def delete(contact_id):
    return render_template('delete.html', contact_id=contact_id)

if __name__ == '__main__':
    app.run(debug=True)

    