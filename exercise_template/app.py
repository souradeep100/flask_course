from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, IntegerField, Form

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class MyForm(Form):
    mail1 = StringField('mail',_name="mail",id='mail')
    submit = SubmitField('submit now')
@app.route('/',methods=['POST','GET'])
def index():
    form = MyForm(request.form)
    if request.method == 'POST'  and 'mail' not in session:
        print("soura")
        email = form.mail1.data
        msg = f"the mail id is {email} "
        flash(msg)
        session['mail'] =  email
        return redirect(url_for('index'))
    return render_template('index.html',form=form)
'''
@app.route('/result')
def result():
    email = request.args.get("email")
    password = request.args.get("password")
    return render_template('result.html',email=email)
'''
if __name__ == "__main__":
     app.run(debug=True)
