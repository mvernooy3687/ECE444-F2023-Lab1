from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp, ValidationError
from datetime import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard tp guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)
@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    email = None
    form = OneForm()
    #form=NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')
        if old_name is not None and old_name!= form.name.data:
            flash('Looks like you have changed your name!')

        if old_email is not None and old_email!= form.email.data:
            flash('Looks like you have changed your email!')
        
        session['name'] = form.name.data
        session['email'] = form.email.data
        email_valid = True if 'utoronto' in session['email'] else False
        return redirect(url_for('index'))
    
    email_valid = False
    if session.get('email'):
        email_valid = True if 'utoronto' in session.get('email') else False
    
    return render_template('index.html',form=form, name=session.get('name'),email=session.get('email'),email_valid=email_valid)

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
    #email = StringField('What is your UofT Email address?', validators=[DataRequired(), Regexp('^\S+@\S+$',message='Please include an \'@\' in the email address. \'{}\' is missing an \'@\''.format(session.get('email')))])#Email(message='Please include an "@"')])
    
    #email = StringField('What is your UofT Email address?', validators=[DataRequired(), Email(message='Please include an "@"')])
    email = StringField('What is your UofT Email address?', validators=[DataRequired()])#, Regexp('^\S+@\S+$')])#Email(message='Please include an "@"')])
    
    submit = SubmitField('Submit')

    def validate_email(self,field):
        if not '@' in field.data:
            raise ValidationError('Please include an \'@\' in the email address. \'{}\' is missing an \'@\''.format(field.data))
