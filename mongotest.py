# -*- encoding:UTF-8 -*-
#http://www.mongoalchemy.org/intro.html
#http://api.mongodb.com/python/current/tools.html
#https://pypi.python.org/pypi
#https://boto3.readthedocs.io/en/latest/guide/quickstart.html
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from pymongo import MongoClient
import datetime
import pprint

from mongoalchemy.document import Document
from mongoalchemy.fields import *
from mongoalchemy.session import Session
import bson
from bson.codec_options import CodecOptions

import sqlalchemy_declarative

client = MongoClient('localhost',27017)
db = client['runoob']
post = {"author":"mike34",
        "text": "my first blog post",
        "data": datetime.utcnow()

}
# posts = db.posts
# post_id = posts.insert_one(post).inserted_id
# print post_id
# pprint.pprint(posts.find_one())
# for post in posts.find():
#     pprint.pprint(post)

class Student(Document):
    name = StringField()
    age = IntField(min_value=0)

session = Session.connect('runoob')
session.clear_collection(Student)

#student = Student(name=unicode('注TETE', 'utf-8'),age=20)
student = Student(name='注水晶89',age=20)
print student.name
session.save(student)
session
#
# import sys
# print sys.getdefaultencoding()




# 1．问题描述：一个在Django框架下使用Python编写的定时更新项目，在Windows系统下测试无误，在Linux系统下测试，报如下错误：
# ascii codec can't decode byte 0xe8 in position 0:ordinal not in range(128)
# 2．原因分析：字符问题。在Windows系统转Linux系统时，字符问题很容易出现。
# 3．解决办法：在出现问题的页加上如下三行即可：
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# 本文实例讲述了Python设置默认编码为utf8的方法。分享给大家供大家参考，具体如下：
# 这是Python的编码问题，设置python的默认编码为utf8
# python安装目录：/etc/python2.x/sitecustomize.py

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
# try:
#   import apport_python_hook
# except ImportError:
#   pass
# else:
#   apport_python_hook.install()
# 如果在windows下：
# 可以在Python安装目录下的Lib/site-packages目录中，新建一个sitecustomize.py文件（也可以建在其它地方，然后手工导入，建在这里，每次启动Python的时候设置将自动生效），内容如下：

# import sys
# sys.setdefaultencoding('utf-8') #set default encoding to utf-8
# 然后可以查看到改变已经生效

# >>> import sys
# >>> sys.getdefaultencoding()
# 'utf-8'
# 此时运行程序，如果仍然报告之前的错误，只需要显示地设定输出的编码

# print s.encode('utf-8')


