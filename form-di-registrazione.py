# app.py
from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'una_chiave_segreta_very_secret'

class RegistrationForm(FlaskForm):
    """
    Form di registrazione
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(message='Email non valida')])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Registrati')
    
    
class LoginForm(FlaskForm):
    """
    Form di login
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Login')
    
class ForgotPasswordForm(FlaskForm):
    """
    Form di Forgot Password
    """
    email = StringField('Email', validators=[DataRequired(), Email(message='Email non valida')])
    submit = SubmitField('Recuperare la password?')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Qui si gestirebbe la registrazione dell'utente (es. salvataggio nel database)
        flash('Registrazione avvenuta con successo!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Registrazione', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Qui si gestirebbe il login dell'utente
        flash('Login avvenuto con successo!', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        # Qui si gestirebbe il recupero della password
        flash('Ti abbiamo inviato un\'email con le istruzioni per recuperare la password', 'info')
        return redirect(url_for('login'))
    return render_template('forgot-password.html', title='Recupera la tua password', form=form)

if __name__ == '__main__':
    app.run(debug=True)
