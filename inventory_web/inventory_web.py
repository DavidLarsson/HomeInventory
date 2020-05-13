from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def default_route():
    return "Default"

@app.route('/<string:category>/')
def category_filter(category):
    return category

@app.route('/add/')
def add_item():
    return "Add item"

@app.route('/shopping/')
@app.route('/shopping/<string:category>/')
def shopping_list(category=None):
    if category == None:
        return "My shopping list"
    else:
        return category

