from flask import render_template, url_for
from trial import app

#Create route for home app
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/blog')
def blog():
    return render_template('blog.html', title='Latest News')

#Create a route for divisions
@app.route('/divisions')
def division():
    return render_template('divisions.html', title='Division')

#Create a route for divisions
@app.route('/basic')
def basic():
    return render_template('basic_temp.html', title='Basic')

#Create a route for divisions
@app.route('/defect')
def defect():
    return render_template('defect_report.html', title='Road Defects Report')