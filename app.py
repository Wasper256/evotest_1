"""Main app file."""
from flask import Flask, render_template, request, flash, redirect
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
        try:  # add name
            name = request.form['name']
            db.session.add(Names(name))
            db.session.commit()
            flash("New name successfully added!")
            return redirect("", code=302)
        except:  # same name exception handler
            db.session.rollback()
            flash("Error! Name already exists!")
    elif request.method == 'POST' and "lucky" in request.form:
        if len(names) < 3:  # random names
            flash("Error! Too few names! Add names and try again!")
        else:
            win = []  # winners selection
            while len(win) < 3:
                n = choice(names).name
                if n in win:
                    pass
                else:
                    n = n.encode("utf-8")
                    win.append(n)
            flash("Winners is: {0}, {1}, {2}.".format(win[0], win[1], win[2]))
    elif request.method == 'POST' and "input_del_name" in request.form:
        idn = request.form["id"]  # delete name
        Names.query.filter_by(id=idn).delete()
        db.session.commit()
        flash("Selected name was deleted")
        return redirect("", code=302)
    return render_template('index.html', names=names)


if __name__ == '__main__':
    app.run(debug=False)
