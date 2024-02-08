from datetime import datetime
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, SelectField
from wtforms.validators import DataRequired

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

#@app.route('/search')
#def search():
#    return render_template('search.html')

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
