from app import app
from flask import Flask, render_template

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def sign_up():
    return render_template('sign_up.html')


@app.route('/signin')
def sign_in():
    return render_template('sign_in.html')


@app.route('/about')
def about():
    return render_template('about.html')
