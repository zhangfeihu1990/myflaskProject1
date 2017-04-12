# -*- encoding:UTF-8 -*-
from flask import Flask,render_template,flash,jsonify
from flask import redirect,request, url_for
from flask_script import Manager
from flask_bootstrap import Bootstrap
#from flask_wtf import 
from wtforms import Form,StringField, SubmitField,validators, BooleanField, PasswordField
#from wtforms.validators import Required
#from sqlalchemy import SQLAlchemy   not ok
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

import os

'''
nav
'''
from flask_nav import Nav
from flask_nav.elements import Navbar, View
nav = Nav()

@nav.navigation()
def mynavbar():
    return Navbar(
        'mysite',
        View('Home', 'register'),
        View('register', 'register'),
    )



from sqlalchemy.orm import sessionmaker 
from sqlalchemy_declarative import Address, Base, Person,Book,MyImage
engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker(bind=engine)

session = DBSession()

#basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
manager = Manager(app)
bootstrap = Bootstrap(app)

Base = declarative_base()
#app.config['SQLALCHEMY_DATABASE_URI'] =\
#'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
  name = None
  form = NameForm()
  name = form.name.data
  form.name.data = ''
  

  person = session.query(Person).first()
  name = person.name
  persons = session.query(Person).all()
  # return render_template('user.html', form=form, name=name,persons=persons)
  return render_template('testreact.html')

@app.route('/user/<name>')
def user(name):
  #return '<h1>Hello, %s!</h1>' % name
  return render_template('user.html',name=name)

@app.route('/redir/')
def redir():
  return redirect('http://www.baidu.com')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm(request.form)
#     if request.method == 'POST' and form.validate():
#         user = User(form.username.data, form.email.data,
#                     form.password.data)
#         db_session.add(user)
#         flash('Thanks for registering')
#         return redirect(url_for('login'))
#     return render_template('register1.html', form=form)

@app.route('/person', methods=['GET', 'POST'])
def person():
    form = PersonForm(request.form)
    if request.method == 'POST' and form.validate():
        print form.name.data
        new_person = Person(name=form.name.data)
        session.add(new_person)
        session.commit()
        print 'hahahah'
        flash('add successful')
        return redirect('/')
    #return redirect('http://www.baidu.com')
    return render_template('person.html', form=form,name='aaaa')

@app.route('/addbook',methods=['GET', 'POST'])
def addbook():
    
    if request.method == 'POST':
        print request.form['price']
        new_book = Book(book_name=request.form['book_name'],price=request.form['price'])
        session.add(new_book)
        session.commit()
        print 'ok ,a book has added'
    return render_template('book.html')
'''
自己的ajax方法
'''
@app.route('/testajax', methods=['GET', 'POST'])
def testajax():
    print request.args
    a = request.args.get('a')
    b = request.args.get('b')
    print a
    print b
    result = a+b
    mylist = [1,2,3,"zhang"]
    return jsonify(mylist)
'''
ajax方法
'''
@app.route('/testajax2')
def testajax2():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    #mylist = [1,2,3,"zhang"]
   # mymap = {a:"zhang",b:"fei",c:"hu"}
    return jsonify(result=a + b)
    #return jsonify(result= mylist)
    #return jsonify(result= mymap)不行
 
'''
ajax方法
'''
@app.route('/testajax3')
def testajax3():
    print 'run:testajax3'
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    #mylist = [1,2,3,"zhang"]
   # mymap = {a:"zhang",b:"fei",c:"hu"}
    return jsonify(result=a + b)
    #return jsonify(result= mylist)
    #return jsonify(result= mymap)不行    
 
@app.route('/show_image')
def show_image():
    images = session.query(MyImage).all()  
    return render_template('show_image.html',images = images)
  
@app.route('/upload_file', methods=['POST','GET'])
def upload_file():
    if request.method == 'POST': 
      print 'aaaaaaaa'      
      file = request.files['file']     
      filename = file.filename
      print os.path.join('uploads/',filename)
      file.save(os.path.join('static/uploads/',filename))
      
      image_url = os.path.join('uploads/',filename)
      image_name=filename
      image = MyImage(image_url=image_url,image_name=image_name)
      session.add(image)
      session.commit()
      print 'image uploaded'
      
      print filename
      return redirect('/')    
    return redirect('/')
@app.route('/testreact')
def testreact():
    print 'reacttest'
    render_template('testreact.html')

nav.init_app(app)  #nav bar    

class NameForm(Form):
  name = StringField('What is your name?')
  submit = SubmitField('Submit')

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])    
    
class PersonForm(Form):
  name = StringField('What is your name?',[validators.DataRequired()])
  #address = StringField('What is your address?')
  submit = SubmitField('Submit')    
    
if __name__ == '__main__':
  #app.run(debug=True)
  manager.run()