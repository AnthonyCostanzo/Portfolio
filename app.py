import sqlite3
from flask import Flask,request,redirect,render_template
import os

currentDirectory = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
@app.route('/')
def render_homepage():
    return render_template('index.html')

@app.route('/<string:pagename>')
def render_works(pagename):
    page = pagename
    return render_template(f'{page}.html',pagelink=page)

@app.route('/submit_form',methods=["GET","POST"])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = str(request.form['email']).strip('@.')
        subject = request.form['subject']
        message = request.form['message']
        connection = sqlite3.connect(currentDirectory+'/contacts.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO contactInfo VALUES(?,?,?,?)',(name,email,subject,message))
        connection.commit()
        return render_template('thankyou.html',name=name)
    else:
        return 'something went wrong.Try again'


