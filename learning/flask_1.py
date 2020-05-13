from flask import Flask, render_template, url_for, request, redirect
from sympy import *
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return "This page wasn't found.", 404

@app.route('/about-me/')
def description():
    return "This is me"

def Fib(n_eval):
    n = symbols("n")
    Fn = (((1+sqrt(5))/2)**n - ((1-sqrt(5))/2)**n)/sqrt(5)
    return expand(Fn.subs(n,n_eval))

def valid_number(number):
    return True

@app.route('/fib/', methods=['POST', 'GET'])
def fibonacci_entry():
    error = None
    if request.method == 'POST':
        number = request.form['number']
        if valid_number(number):
            return redirect(url_for('fibonacci', n=number))
    else:
        return render_template('fibonacci.html')

@app.route('/fib/<int:n>')
def fibonacci(n):
    fibonacci = { 'n': n, 'fib': Fib(n) }
    return render_template('fibonacci.html', fibonacci=fibonacci)

@app.route('/')
def default_route():
    navigation = [ {'href': url_for('description'),
                    'caption': "Who am I?"},
                   {'href': url_for('fibonacci_entry'),
                    'caption': "Fibonacci" },
                   {'href': url_for('fibonacci', n=50),
                    'caption': "Fibonacci #50"} ]
    return render_template('index.html', navigation=navigation)
