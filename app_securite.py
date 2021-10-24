# app.py
from flask_login import login_required
from flask import Blueprint, Flask,redirect,url_for
from __init__ import create_app

app = create_app()
@app.route('/', methods=['POST','GET'])
@login_required
def index():
	return 	redirect(url_for('index.html'))

if __name__ == "__main__":
 app.run(host= 'localhost',port = 5000,debug=True)