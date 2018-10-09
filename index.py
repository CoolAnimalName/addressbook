from flask import Flask, render_template, request
import pymysql

db = pymysql.connect(host='localhost', user='root', password='hi', db='contact_list_db')
cur = db.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    cur.execute("SELECT * FROM contact WHERE FName='Hogan';")
    data = list(cur)
    field_names = [i[0] for i in cur.description]
    length = len(data[0])
    return render_template('index.html', data=data, field_names=field_names, length=length)

@app.route('/form')
def form():
    cur.execute("SELECT * FROM contact WHERE FName='Hogan';")
    data = cur.fetchall()
    return render_template('form.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

    