from flask import Flask, request, render_template, redirect, url_for, flash,get_flashed_messages
from forms import RegistrationForm, LoginForm
import pdb


app = Flask(__name__)
app.config['SECRET_KEY'] = '09ebf1e8b75d8c34977c092fc880f7b2'

posts = [
    {
        'author': "Alireza",
        'title': "My First Post",
        'content': "This is the first post.",
        'createdAt': "29 Dec,2026"
    },
    {
        'author': "Abbas",
        'title': "My Second Post",
        'content': "This is my first post",
        'createdAt': "29 Dec,2026"
    },
    {
        'author': "Zahra",
        'title': "My Third Post",
        'content': "This is my first post",
        'createdAt': "29 Dec,2026"
    },
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    title = "Registeration"
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!","success")
        return redirect(url_for('home'))
    return render_template('register.html', title=title, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    title = "Login"
    if form.validate_on_submit():
        flash(f"Logged In - Succcessfully {form.email.data}!","success")
        return redirect(url_for('home'))
    return render_template('login.html', title=title, form=form)
