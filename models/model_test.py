# -*- coding: utf-8 -*-
from models import *
class TestUser(Base):
    __tablename__ = 'test_user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    profile = Column(String(50))

    def __repr__(self):
        return '<TestUser %r>' % (self.id)
