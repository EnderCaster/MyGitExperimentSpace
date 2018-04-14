# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from faker import Factory
import random
engine = create_engine('mysql+mysqldb://root@localhost:3306/blog?charset=utf8')
Base=declarative_base()
article_tag = Table(
	# The first parameter means table name, and the second is metadata ,the two is requied
	'article_tag',Base.metadata,
	# as for a auxiliary table generally save the two tables' id and set to foreign key
	Column('article_id',Integer,ForeignKey('articles.id')),
	Column('tag_id',Integer,ForeignKey('tags.id'))
)
class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)
class User(Base):
	__tablename__ ='users'
	""" same to sql but use , to split keywords 
	and use _ to connect in keyword
	the variable name equals to Column name. """
	id = Column(Integer, primary_key=True)
	username = Column(String(64),nullable=False,index=True)
	password = Column(String(64), nullable=False)
	email = Column(String(64),nullable=False, index=True)
	# one to many
	articles = relationship('Article',backref='author')
	# set uselist to false means one to one
	userinfo = relationship('UserInfo',backref='user',uselist=False)
	def __repr__(self):
		return '%s(%r)' % (self.__class__.__name__,self.username)
class UserInfo(Base):

    __tablename__ = 'userinfos'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    qq = Column(String(11))
    phone = Column(String(11))
    link = Column(String(64))
    user_id = Column(Integer, ForeignKey('users.id'))
class Article(Base):
	__tablename__ ='articles'
	id = Column(Integer, primary_key=True)
	title = Column(String(255), nullable=False, index=True)
	content = Column(Text)
	user_id = Column(Integer , ForeignKey('users.id'))
	def __repr__(self):
		return '%s(%r)' % (self.__class__.__name__,self.title)
engine = create_engine('mysql+mysqldb://root@localhost:3306/blog?charset=utf8')
faker = Factory.create()
Session = sessionmaker(bind=engine)
session = Session()
faker_users=[User(
	username=faker.name(),
	password=faker.word(),
	email=faker.email()
) for i in range(10)]
session.add_all(faker_users)
faker_tags= [Tag(name=faker.word()) for i in range(20)]
session.add_all(faker_tags)
for i in range(100):
    article = Article(
    title=faker.sentence(),
    content=' '.join(faker.sentences(nb=random.randint(10, 20))),
    )
session.commit()
