from flask_login import login_user,logout_user,login_required
from flask import render_template,redirect,url_for, request, flash
from ..models import User
from .forms import LoginForm,RegistrationForm
from . import auth
from .. import db