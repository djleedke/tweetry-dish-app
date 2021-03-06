from flask import Flask
from flask_sqlalchemy import SQLAlchemy, utils
from flask.cli import with_appcontext
import click

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from application.tweetry_manager import TweetryManager
tweetry_manager = TweetryManager()

from application import routes

@click.command(name='create_new_tweetry')
@with_appcontext
def create_new_tweetry():
    tweetry_manager.create_new_tweetry()
    print('New Tweetry created.')

@click.command(name='check_quotes')
@with_appcontext
def check_quotes():
    tweetry_manager.check_for_new_quotes()
    print('Quote check complete.')

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()
    tweetry_manager.check_for_new_quotes()
    tweetry_manager.create_new_tweetry()
    print('Tables created.')

@click.command(name='drop_tables')
@with_appcontext
def drop_tables():
    db.drop_all()
    print('Tables dropped.')

app.cli.add_command(create_new_tweetry)
app.cli.add_command(check_quotes)
app.cli.add_command(create_tables)
app.cli.add_command(drop_tables)



