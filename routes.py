from app import app
import os

version = os.getenv('VERSION_STR', '0.4.57')

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World! " + version
	# @TODO see the other exampe-* apps for additional examples.
	# NOTICE: please fork this to your own repo before committing.
