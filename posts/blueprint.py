from flask import Blueprint, render_template

from models import Post
posts = Blueprint('posts', __name__, template_folder='templates')
@posts.route('/')
def index():
    # posts = Post.query.all()
    return render_template('posts/index.html')

@posts.route('/create')
def create_post():
    return render_template('posts/creation.html')

# @posts.route('/<slug>')
# def post_detail(slug):
#     post = Post.query.filter(Post.slug == slug).first()
#     return render_template('posts/post_detail.html', posts=posts)