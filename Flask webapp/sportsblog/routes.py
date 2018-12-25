from flask import render_template, url_for, flash, redirect
from sportsblog import app, db, bcrypt
from sportsblog.forms import RegistrationForm, LoginForm
from sportsblog.models import User, Post


posts = [
    {
        'author': 'Sai Harshith',
        'title': 'Messi is the GOAT.',
        'content': 'After a remarkable 2018, leading all the football charts. He is undoubtedly the best player of all time ',
        'date_posted': 'December 20, 2018'
    },
    
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()        
        flash(f'Your Account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)