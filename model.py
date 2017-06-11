# -*- encoding:UTF-8 -*-
from mongoalchemy.document import Document
from mongoalchemy.fields import *

class News(Document):
     title =  StringField()
     update_time = StringField()
     author = StringField()
     content = StringField()

     # def __init__(self, title, update_time, author, content):
     #     self.title = title
     #     self.update_time = update_time
     #     self.author = author
     #     self.content = content



