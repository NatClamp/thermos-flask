from flask import Flask, render_template, url_for

app = Flask(__name__)

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def initials(self):
        return "{}. {}.".format(self.firstname[0], self.lastname[0])

@app.route('/')
def index():
    return render_template('index.html', text='It would make me happy if you were happy.', title='How do you do?', user=User("Natalie", "Clamp"))

@app.route('/add')
def add():
    return render_template('add.html')

if __name__ == "__main__":
    app.run()
