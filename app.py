# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 10:51:12 2023

@author: E40052158
"""

from flask import Flask, render_template,request, flash
app = Flask(__name__)
app.secret_key = "raki@123"
@app.route("/hello")
def index():
    flash("who is your favourite player?")
    return render_template('index2.html')
@app.route("/greet",methods = ["POST","GET"])
def greet():
    flash("Wow "+ str(request.form['name_input'])+ " is a great player")
    return render_template('index2.html')
if __name__ == '__main__':
   app.run()