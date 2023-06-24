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
            flash("Sign Up Successfully",category='success')
            pass
    return render_template('signup.html')
