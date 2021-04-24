from flask import Flask, redirect, render_template

from funcs import get_page

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def index():
    page = get_page()
    context = {
        'title': page.title,
        'url': page.fullurl,
        'summary': page.summary,
    }
    return render_template('index.html', **context)
