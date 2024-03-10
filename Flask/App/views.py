import sys, subprocess, logging
from flask import Flask, render_template, request, redirect, flash, url_for
from .ganache import *


app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/')
@app.route('/VotinCorpo')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        company = request.form['company']
        position = request.form['position']
        email = request.form['email']
        address = request.form['address']
        return redirect('/login')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        address = request.form['address']
        pk = request.form['pk']
        accounts = get_accounts()
        if accounts:
            if address in accounts:
                if accounts[address] == pk:
                    return redirect('/MyElectorSpace')
                else:
                    flash("Invalid private key!")
            else:
                flash("Invalid Address...")
        else:
            flash("Blockchain unreachable, make sure that ganache is launched")

    return render_template('login.html')


@app.route('/MyElectorSpace', methods=['GET'])
def elector():
    return render_template('elector.html', user = data)


@app.route('/elections')
def elections():
    return render_template('elections.html')
