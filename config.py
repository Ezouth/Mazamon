import os
# imports operating system library which allows us to create paths on either harddrive or other peoples
basedir = os.path.abspath(os.path.dirname(__file__))
#baseddir stands for based directory. We are finding the absolute path to that file
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
