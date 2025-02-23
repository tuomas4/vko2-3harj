"""Example miniature HTTP server application using flask."""


from flask import Flask


import palvelin.pages


app = Flask(__name__)


@app.route("/")
def index():
    return palvelin.pages.indexPage


@app.route("/page1")
def pageone():
    return palvelin.pages.pageOne


@app.route("/page2")
def pagetwo():
    return palvelin.pages.pageTwo


@app.route("/page3")
def pagethree():
    return palvelin.pages.pageThree
