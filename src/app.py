from flask import Flask, render_template
from helpers.common import translation

app = Flask(__name__)
@app.route("/")
def hello_world():
    locales, t  = translation(['demo'])
    return render_template('hello.html',t=t, locales=locales['demo'])