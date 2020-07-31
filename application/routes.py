from application import app
from flask import render_template


dummyData = [
{
"name": {"band":"The Kooks"},
"title":"First Post",
"city":"Sheffield",
"content":"Description of gig for exampe what tour/genres"
},
{
"name": {"band":"The Kaleidoscopess"},
"title":"Another Post",
"city":"Manchester",
"content":"Description of gig for exampe what tour/genres"
},
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home', posts=dummyData)

@app.route('/city')
def city():
    return render_template('city.html', title='city')
@app.route('/register')
def register():
    return render_template('register.html', title='Register')
@app.route('/login')
def login():
    return render_template('login.html', title='Login')

