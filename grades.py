#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, redirect, session, flash
# import sqlite3

app = Flask(__name__)
app.secret_key = 'Keep this a secret'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'user' in session:
        return redirect('/dashboard')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            session['user'] = username
            flash('Login successful!', 'Success')
            return render_template('/dashboard')
        else:
            flash('Login failed.', 'Error')
            return render_template('login.html')
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run()