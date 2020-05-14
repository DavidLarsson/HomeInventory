from flask import Flask, render_template, url_for, request, redirect
import shelve

app = Flask(__name__)
d = shelve.open("storage")


@app.route("/")
def default_route():
    return "Default"


@app.route("/<string:category>/")
def category_filter(category):
    return category


@app.route("/add/")
def add_item():
    return "Add item"


@app.route("/shopping/")
@app.route("/shopping/<string:category>/")
@app.route("/shopping/<string:category>/<string:itemtype>/")
def shopping_list(category=None, itemtype=None):
    if category == None:
        return "My shopping list"
    elif itemtype == None:
        return category
    elif itemtype in items(category):
        return itemtype


d.close()
