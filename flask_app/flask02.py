# FLASK Tutorial 1 -- We show the bare bones code to get an app up and running

# imports
import os                 # os is used to get environment variables IP & PORT
<<<<<<< HEAD
from flask import Flask   # Flask is the web app that we will customize
from flask import render_template
=======
from flask import render_template   # Flask is the web app that we will customize
>>>>>>> d6054bbd3396e102cc26e433b380c94deb9c2d24

app = Flask(__name__)     # create an app

# @app.route is a decorator. It gives the function "index" special powers.
# In this case it makes it so anyone going to "your-url/" makes this function
# get called. What it returns is what is shown as the web page
<<<<<<< HEAD
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
=======
@app.route('/index')
def index():
    return render_template('index.html’)
>>>>>>> d6054bbd3396e102cc26e433b380c94deb9c2d24


app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)

# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000

# Note that we are running with "debug=True", so if you make changes and save it
# the server will automatically update. This is great for development but is a
# security risk for production.