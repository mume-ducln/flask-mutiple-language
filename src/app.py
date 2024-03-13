from flask import Flask, render_template
from helpers.common import getLocales

app = Flask(__name__)
@app.route("/")
def hello_world():
    locales = getLocales(['demo'])
    return render_template('hello.html',demo=locales['demo'], currentLocale=locales['currentLocale'])