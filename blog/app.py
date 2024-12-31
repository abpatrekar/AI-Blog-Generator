from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from models import User, BlogPost, db
from ai_module import generate_blog_post
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['POSTS_PER_PAGE'] = 10
db.init_app(app)

# Routes
@app.route('/')
def index():
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.get(user_id)
        return render_template('index.html', user=user)
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Registered successfully! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/generate_post', methods=['POST'])
def generate_post():
    if 'user_id' in session:
        topic = request.form['topic']
        user_id = session['user_id']
        user = User.query.get(user_id)
        content = generate_blog_post(topic)
        post = BlogPost(title=topic, content=content, author=user)
        db.session.add(post)
        db.session.commit()
        flash('Blog post generated successfully!', 'success')
    else:
        flash('You need to login to generate a post', 'error')
    return redirect(url_for('index'))

@app.route('/history')
def history():
    if 'user_id' not in session:
        flash('You need to login to view history', 'error')
        return redirect(url_for('index'))
    user_id = session['user_id']
    user = User.query.get(user_id)
    page= request.args.get('page',1,type=int)
    posts = BlogPost.query.filter_by(author_id=user.id).paginate(page=page, per_page=app.config['POSTS_PER_PAGE'], error_out=False)


    if not posts.items:
        flash('No posts found', 'info')
        return redirect(url_for('index'))
    return render_template('history.html', posts=posts)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)