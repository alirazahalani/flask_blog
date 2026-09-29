import flask

app = flask.Flask(__name__)

posts = [
    {
        'author': "Alireza Halani",
        'title' : "My First Post",
        'content' : "This is the first post.",
        'createdAt' : "29 Dec,2026"
    },
    {
        'author': "Abbas",
        'title' : "My Second Post",
        'content' : "This is my first post",
        'createdAt' : "29 Dec,2026"
    },
    {
        'author': "Zahra",
        'title' : "My Third Post",
        'content' : "This is my first post",
        'createdAt' : "29 Dec,2026"
    },
]

@app.route('/')
@app.route('/home')
def home():
    return flask.render_template('home.html', posts=posts) 

@app.route('/about')
def about():
    return flask.render_template('about.html') 

@app.route('/register')
def register():
    return flask.render_template('register.html') 

@app.route('/login')
def login():
    return flask.render_template('login.html') 
