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