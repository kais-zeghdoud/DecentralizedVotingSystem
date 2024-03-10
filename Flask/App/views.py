import sys, subprocess, logging
from flask import Flask, render_template, request, redirect, flash, url_for
from .ganache import *

# data en dur à supprimer plus tard
data = {'name': "kais",
        'company': "efrei",
        'position': "dev",
        'email': 'kais.zeghdoud@efrei.net',
        'address': '0x95222290DD7278Aa3Ddd389Cc1E1d165CC4BAfe5',
        'pk': '0x999999cf1046e68e36E1aA2E0E07105eDDD1f08E',
        'votes': 0}

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
        elector = (name, company, position, email, address)
        # appel fonction solidity : constructor of Elector
        print(elector)
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
