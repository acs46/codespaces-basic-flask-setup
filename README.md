BasicFlaskSetup

Simple framework w/ Navigation Menu

$ pip3 list # lists currently installed modules

Create a project directory for your stuff
$ cd ~/mydir
Unzip BasicFlaskSetup.zip
$ create .gitignore (for any files don't need in repo)
$ git init

Virtual Environments

Creates venv directory in your project directory
$ python3 -m venv venv # could call the virtual env something else i.e. python3 -m venv myenviro
$ source venv/bin/activate # activate the virtual environment in your current project dir
$ deactivate # deactivate turns off virtual environment

for python2
$ sudo pip install virtualenv
$ virtualenv venv

for Windows environment run as Admin
$ pip install virtualenv
$ virtual venv
$ venv\Scripts\activate

$ pip3 install flask
or
$ pip install flask
$ pip3 freeze # shows all packages installed in virtual env

Make sure all the packages in requirements file are installed for this example to work

$ pip3 install -r requirements.txt ## install all packages for basicflasksetup to run application

$ pip3 freeze > requirements.txt #will create file 'requirements.txt' listing all packages currently loaded
Part 1 - Create the app

create mydir/1main.py

  from flask import Flask

  app = Flask(__name__)

  @app.route("/")
  def home():
      return "Hello, World!"

  @app.route("/ash")
  def ash():
      return "Hello, Ash!"

  if __name__ == "__1main__":
      app.run(debug=True)

$ export FLASK_APP=1main.py

start local server

$ flask run

    Running on http://127.0.0.1:5000/

or

$ python 1main.py

    Running on http://127.0.0.1:5000/

open web browser to http://127.0.0.1:5000 (or localhost:5000)
control+C in the terminal window to quit server
Part2 - Add a template page to app

Create a new version of the app called 2main.py and a template called templates/home1.html

$vi 2main.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home1.html")

@app.route("/ash")
def ash():
    return "Hello, Ash!"

if __name__ == "__2main__":
    app.run(debug=True)

create a directory mydir/templates
inside templates directory create file home1.html

  <!DOCTYPE html>
  <html lang="en" dir="ltr">

  <title>First Flask Page</title>

   <div class="page-header">
    <h1> My Awesome Bioinformatics Project </h1>
    <p> Flask is Functional </p>
    <h1>Hello World!</h1>

   </div>
  </html>

$ export FLASK_APP=2main.py

start local server
$ flask run

    Running on http://127.0.0.1:5000/

open web browser to http://127.0.0.1:5000
(or localhost:5000)
control+C in the terminal window to quit server
Part 3 - Add another route (about) and a navigation menu using bootstrap

Create a new version of the app called 3main.py and a template called templates/about.html

$vi 3main.py

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/ash")
def ash():
    return "Hello, Ash!"

if __name__ == "__3main__":
    app.run(debug=True)

inside templates directory create file about.html
vi about.html

  <!DOCTYPE html>
  <html lang="en" dir="ltr">

  <title>First Flask Page</title>

   <div class="page-header">
    <h1> My Awesome Bioinformatics Project </h1>
    <p> Flask is Functional </p>
    <h1>Hello World!</h1>

   </div>
  </html>

$ export FLASK_APP=3main.py

start local server
$ flask run

    Running on http://127.0.0.1:5000/

open web browser to http://127.0.0.1:5000
(or localhost:5000)
control+C in the terminal window to quit server
Part 4 - Add more routes pg2, search, refs, help and use form to catch user input and add error pages

Create a new version of the app called main.py and a template called templates/pg2 search ref help etc.

$vi main.py from datetime import datetime from flask import Flask, render_template from flask_bootstrap import Bootstrap from flask_moment import Moment from flask_wtf import FlaskForm from wtforms import StringField, RadioField, SubmitField, SelectField from wtforms.validators import DataRequired

app = Flask(__name__) 
app.config['SECRET_KEY'] = 'thequickbrownfrog' 
 
bootstrap = Bootstrap(app) 
moment = Moment(app) 
 
class NameForm(FlaskForm): 
    name  = StringField('Enter a search term:', validators=[DataRequired()]) 
    name2 = StringField('Enter a another term', validators=[DataRequired()]) 
    name3 = RadioField('Enter a term', choices=[('r','Red'),('y','Yellow'),('b','Blue')]) 
    name4 = SelectField('Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')]) 
 
    submit = SubmitField('Submit') 
 
@app.errorhandler(404) 
def page_not_found(e): 
    return render_template('404.html'), 404 
 
@app.errorhandler(500) 
def internal_server_error(e): 
    return render_template('500.html'), 500 
 
@app.route('/') 
def home(): 
    return render_template('home.html',current_time=datetime.utcnow()) 
 
@app.route('/about') 
def about(): 
    return render_template('about.html') 
 
@app.route('/pg2') 
def pg2(): 
    return render_template('pg2.html') 
 
@app.route('/ref') 
def ref(): 
    return render_template('ref.html') 
 
@app.route('/help') 
def help(): 
    return render_template('help.html') 
 
@app.route('/search', methods=['GET', 'POST']) 
def search(): 
    name  = None 
    name2 = None 
    name3 = None 
    name4 = None 
    form = NameForm() 
    if form.validate_on_submit(): 
	name = form.name.data 
	name2 = form.name2.data 
	name3 = form.name3.data 
	name4 = form.name4.data 
	form.name.data = '' 
	form.name2.data = '' 
	form.name3.data = '' 
	form.name4.data = '' 
    return render_template('search.html', form=form, name=name, name2=name2) 
 
if __name__ == "__main__": 
    app.run(debug=True) 

inside templates directory new pages are created for pg2 search ref help errors etc

$ export FLASK_APP=main.py

start local server
$ flask run

    Running on http://127.0.0.1:5000/

open web browser to http://127.0.0.1:5000
(or localhost:5000)
control+C in the terminal window to quit server

Save changes using git
git add .
git commit -m "finished editing"

Deactivate virtual environment when you're finished
$ deactivate

