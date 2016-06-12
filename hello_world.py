from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def say_hi():
    return "Hello, world!"
    
@app.route('/hello/<name>')
def hi_person(name):
    return render_template('template.html', name = name)
    
@app.route('/hello/<first>/<last>')
def jedi_name(first, last):
    return render_template('template.html', first = first, last = last)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 8080)