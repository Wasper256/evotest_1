"""Main app file."""
from flask import Flask, render_template, request, flash
from extentions import db

app = Flask(__name__)
app.secret_key = 'i_want_in_evo_so_much'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///evo.db'
db.init_app(app)
from models import *


@app.route('/', methods=['GET', 'POST'])
def home():
    """Loading main page."""
    if request.method == 'POST' and request.form['name']:
        print("fsfsfs")
        try:  # simple getting data from forms
            name = request.form['name']
            print("dsfsdfsdf")
            db.session.add(Names(name))
            print("dsfsf")
            db.session.commit()
            print("sfsdfsdf")
            flash("New name successfully added!")
        except:  # anticlone department logic
            flash("Error! Name already exists!")
    else
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
