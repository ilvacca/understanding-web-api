from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def to_dict(self):
        output = {}
        attributes = list(self.__dict__.keys())[1:]
        for attribute in attributes:
            output[attribute] = self.__getattribute__(attribute)
        return(output)
    
    def __repr__(self):
        return "<User(id='%s', name='%s', age='%s')>" % (self.id, self.name, self.age)