from flask import render_template, redirect, request, url_for, abort
from flask_login import login_required, current_user

from . import main
from ..admin import admin
from .forms import ReviewForm, BlogForm, EditBlog, DeleteBlog, DeleteComment
from ..models import Blog, Review, User,Quote
from .. import db



@main.route('/')
def index():

    blogs = Blog.get_blog(id)

    return render_template('index.html', blogs=blogs)


@admin.route('/dashboard')
@login_required

def check_user():

    if current_user.id != 1:
        abort(403)

    return render_template('admin/dashboard.html')


@main.route('/blog/<int:id>')

def single_blog(id):

    single_blog = Blog.query.get(id)

    reviews = Review.get_reviews(id)

    if single_blog is None:
        abort (404)

    return render_template('blog.html', blog=single_blog, reviews=reviews)
