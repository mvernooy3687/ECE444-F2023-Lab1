from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp
from datetime import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard tp guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)
@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    #form = OneForm()
    form=NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        #old_email = session.get('email')
        if old_name is not None and old_name!= form.name.data:
            flash('Looks like you have changed your name!')

        #if old_email is not None and old_email!= form.email.data:
            #flash('Looks like you have changed your email!')
        
        session['name'] = form.name.data
        #session['email'] = form.email.data
        return redirect(url_for('index'))       
    return render_template('index.html',form=form, name=session.get('name'))#,email=session.get('email'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EmailForm(FlaskForm):
    email = StringField('What is your UofT Email address?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class OneForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your UofT Email address?', validators=[DataRequired(), Regexp('^\S+@\S+$',message='Please include an \'@\' in the email address. \'{}\' is missing an \'@\''.format('test'))])#Email(message='Please include an "@"')])
    submit = SubmitField('Submit')
