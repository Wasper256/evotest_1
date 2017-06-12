"""Main app file."""
from flask import Flask, render_template, request, flash
from extentions import db
from random import choice

app = Flask(__name__)
app.secret_key = 'i_want_in_evo_so_much'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///evo.db'
db.init_app(app)
from models import *


@app.route('/', methods=['GET', 'POST'])
def home():
    """Loading main page."""
    names = Names.query.all()
    if request.method == 'POST' and "name" in request.form:
        try:  # simple getting data from forms
            name = request.form['name']
            db.session.add(Names(name))
            db.session.commit()
            flash("New name successfully added!")
        except:  # anticlone department logic
            flash("Error! Name already exists!")
    elif request.method == 'POST' and "lucky" in request.form:
        win = []
        while len(win) < 3:
            n = choice(names).name
            if n in win:
                print"1"
                pass
            else:
                n = n.encode("utf-8")
                win.append(n)
        flash("Winners is: {0}, {1}, {2}.".format(win[0], win[1], win[2]))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
