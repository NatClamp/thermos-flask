from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime
import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config.config["SECRET_KEY"]

bookmarks = []

def store_bookmark(url):
    bookmarks.append(dict(
        url = url,
        user = 'Natalie',
        date = datetime.utcnow()
    ))

def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]

@app.route('/')
def index():
    return render_template('index.html', new_bookmarks=new_bookmarks(5))

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmark(url)
        flash('Stored bookmark "{}"'.format(url))
        return redirect(url_for('index'))
    return render_template('add.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run()
