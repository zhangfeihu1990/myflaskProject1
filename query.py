from sqlalchemy_declarative import Person, Base, Address,Book
from sqlalchemy import create_engine
engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()
# Make a query to find all Persons in the database
print session.query(Person).all()
person = session.query(Person).first()
print person.name
# Find all Address whose person field is pointing to the person object
print session.query(Address).filter(Address.person == person).all()
# Retrieve one Address whose person field is point to the person object
print session.query(Address).filter(Address.person == person).one()
address = session.query(Address).filter(Address.person == person).one()
print address.post_code

books = session.query(Book).all()
for book in books:
  print book.book_name,book.price