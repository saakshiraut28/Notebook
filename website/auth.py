from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_required,login_user,logout_user,current_user

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        pass1 = request.form.get('password')
    
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,pass1):
                flash("Welcome back :)",category='success')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect Password.",category='error')
        else:
            flash("User doesn't exists",category='error')
    return render_template('/login.html',user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@auth.route('/signup',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('username')
        email = request.form.get('email')
        pass1 = request.form.get('password1')
        pass2 = request.form.get('password2')
        
        if len(name) < 2:
            flash("Length of username should be minimum 2 characters.",category='error')
        elif len(email) < 3:
            flash("Length of email should be minimum 3 characters.",category='error')
        elif pass1 != pass2:
            flash("Password doesn't match.",category='error')
        elif len(pass1) <7:
            flash("Password should consist of min 7 characters.",category='error') 
        else:
            new_user = User(username=name,email=email,password=generate_password_hash(pass1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user,remember=True)
            flash("Sign Up Successfully",category='success')
            return redirect(url_for('views.home'))
    return render_template('signup.html',user = current_user)
