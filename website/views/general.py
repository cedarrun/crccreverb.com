from website import app
from flask import Blueprint, render_template, session, redirect, url_for, \
        request, abort

mod = Blueprint('general', __name__)


@mod.route('/about')
def about(name=None):
  return render_template('general/about.html', name=name)

@mod.route('/what-we-believe')
def believe(name=None):
  return render_template('general/believe.html', name=name)

@mod.route('calendar')
def calendar(name=None):
  return render_template('general/calendar.html', name=name)

@mod.route('/contact')
def contact(name=None):
  return render_template('general/contact.html', name=name)

@mod.route('/pictures')
def pictures (name=None):
  return render_template('general/pictures.html',name=name)

@mod.route('/team')
def team(name=None):
  return render_template('general/team.html', name=name)
