import sys, subprocess, logging
from flask import Flask, render_template, request, redirect, flash, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./../html/index.html')
