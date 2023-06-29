from flask import Blueprint,render_template,request,flash, redirect,url_for
from flask_login import login_required,current_user
from .models import Note
from . import db

views = Blueprint('views',__name__)

# Home page
@views.route('/')
def home():
    return render_template("home.html",user=current_user)

@views.route('/dashboard',methods=['GET','POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note)<1:
            flash('Note too small.',category='error')
        else:
            new_note = Note(note=note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note Added',category='success')
    
    return render_template("dashboard.html",user=current_user)


@views.route('/delete',methods=['GET','POST'])
@login_required
def delete():
    if request.method == 'POST':
        note = request.form.get('note_id')
        note_id = request.form.get("note_id")
        note = Note.query.filter_by(id=note_id).first()
        db.session.delete(note)
        db.session.commit()    
        return redirect(url_for('views.dashboard'))
