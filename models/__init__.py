# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATETIME, Text, ForeignKey, PickleType
from sqlalchemy.ext.mutable import MutableDict
import datetime
from mutable import MutableList, MutableSet 

try:
    from config import RDS_HOST, RDS_NAME, RDS_PASS, RDS_DB
    print '---------------mysql------------------'
except:
    RDS_HOST = RDS_NAME = RDS_PASS = ''
    print '---------------sqlite-----------------'

if RDS_HOST:
    engine = create_engine("mysql://%s:%s@%s/%s" % (RDS_NAME, RDS_PASS, RDS_HOST, RDS_DB), encoding='latin1', echo=True)
else:
    engine = create_engine('sqlite:///airbb.db', convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

#qucik flush for db
def flush(db_obj=None):
    if db_obj:
        db_session.add(db_obj)
    db_session.commit()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    #import yourapplication.models
    Base.metadata.create_all(bind=engine)
