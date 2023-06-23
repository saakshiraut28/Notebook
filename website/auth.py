from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return '<h1>Logout</h1>'

@auth.route('/signup',methods=['GET','POST'])
def sign_up():
    if request == 'POST':
        name = request.form.get('username')
        email = request.form.get('email')
        pass1 = request.form.get('password1')
        pass2 = request.form.get('password2')
        if len(name)<1:
            flash('Name should contain more than 1 character', category='error')
        elif len(email)<3:
            flash('Email should contain more than 3 character', category='error')
        elif len(pass1)<7:
            flash('Name should contain more than 7 character', category='error')
        elif pass1 != pass2:
            flash('Password doesn\'t match :(', category='error')
        else:
            flash('You created a new account', category='success')
            pass
    return render_template('signup.html')