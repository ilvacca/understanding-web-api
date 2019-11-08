import sqlalchemy
from sqlalchemy import create_engine
from .models import User
from config import Config
from sqlalchemy.orm import sessionmaker

class DAO:

    def __init__(self):
        self.DATABASE_PATH = Config.DATABASE_PATH
        db_path = "sqlite:///" + self.DATABASE_PATH
        self.engine = create_engine(db_path)
        
    ## DATABASE CONNECTIONS ###############################################################################

    def openDBSession(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return(session)

    def closeDBSession(self, session):
        session.close()

    ## DATABASE QUERIES ###################################################################################

    def getAllUsersFromDB(self):
        session = self.openDBSession()
        queryResult = session.query(User).all()
        self.closeDBSession(session)
        return(queryResult)

    def getUserById(self, id):
        session = self.openDBSession()
        queryResult = session.query(User).filter_by(id=id).all()
        self.closeDBSession(session)
        return(queryResult)

    ## DATABASE INSERT ####################################################################################

    def addUserToDB(self, id, name, age):
        newUser = User(id=id,name=name,age=age)
        print("Trying inserting %s in the DB" % newUser)
        try:
            session = self.openDBSession()
            session.add(newUser)
            session.commit()
            print("Inserted %s in the DB" % newUser)
            self.closeDBSession(session)
            return(True)
        except:
            print("Failing inserting %s in the DB" % newUser)
            return(False)
        