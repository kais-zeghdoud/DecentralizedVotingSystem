import sys, subprocess, logging
from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)

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


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/MyElectorSpace')
def elector():
    return render_template('elector.html')


@app.route('/elections')
def elections():
    return render_template('elections.html')
