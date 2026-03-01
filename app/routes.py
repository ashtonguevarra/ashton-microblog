from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ashton'}
    posts = [
        {
            'author': {'username': 'Dom'},
            'body': 'I pissed my pants today.'
        },
        {
            'author': {'username': 'Tonee'},
            'body': 'I think I have a crush on Ashton.'
        },
        {
            'author': {'username': 'Pau'},
            'body': 'so uhh we broke up...'
        },
        {
            'author': {'username': 'Drei'},
            'body': 'best night ever with robie!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

