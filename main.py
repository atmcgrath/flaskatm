from flask import Flask
from markupsafe import escape
from flask import render_template
import requests
import csv
#import random
#from lxml import html, etree

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('home.html')
# def index():
#     return "<html><h1>Congratulations, it's a web app!</h1><p>To use this app, enter a farenheit number.</p></html>"

@app.route('/astros/')
def get_iss_people():
    response = requests.get("http://api.open-notify.org/astros.json")
    if (response.status_code == 200):
        full = response.json()
        people = full['people']
        astro_names = [p['name']for p in people]
        return render_template('astros.html', names=astro_names)
    else:
        return 'Not found'
@app.route('/jane/')
#@app.route('/jane/<num>')
def lady_susan():
    with open('data/lady-susan.csv', 'r') as f:
        csv_reader = csv.reader(f)
        list_of_csv = list(csv_reader)
        text = '<h2>Lady Susan</h2>\n<ul>'
        for line in list_of_csv[1:]:
            l = '<li>'+ line[0] + '. ' + line[2] + '</li>\n'
            text+= l
        text += '</ul>'
        return render_template('misc.html', text=text)
            

#     text = response.text
#     paragraphs = text.split('/r/n')
#     r = random.randint(0, len(paragraphs)-1)
#     selection = paragraphs[r]
#     return render_template('misc.html', text=selection)
#     #return selection

@app.route('/hello/')
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html', person=name)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)