import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or '_DtDBEyyD_zD8wndyWIz7WRjYNET-dmen7mB6dQNqnQ'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	                          'sqlite:///' + os.path.join(basedir, 'cointrack.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = True
