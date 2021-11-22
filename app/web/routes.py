from flask.helpers import url_for
from web import app, db
from flask import render_template, redirect
from web.forms import MyForm
from web.models import User


@app.route('/', methods = ['GET', 'POST'])
def home_page():
    form = MyForm()
    if form.validate_on_submit():
        u1 = User(name = form.name.data)
        db.session.add(u1)
        db.session.commit()
        return redirect(url_for('home_page'))
    users = User.query.all()
    return render_template('base.html', form = form, users = users)