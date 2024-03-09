import sys, subprocess, logging
from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)

@app.route('/VotinCorpo')
def index():
    return render_template('index.html')


@app.route('/register')
def register():
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
