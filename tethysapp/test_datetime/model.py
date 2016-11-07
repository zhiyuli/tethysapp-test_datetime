# Put your persistent store models in this file
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker

from .app import TestDatetime

from datetime import datetime
import logging
logger = logging.getLogger(__name__)

engine = TestDatetime.get_persistent_store_engine('test_datetime_db_engine')
SessionMaker = sessionmaker(bind=engine)
Base = declarative_base()

# DateTime_Format = '%Y-%m-%dT%X.%f'
DateTime_Format = '%Y-%m-%dT%H:%M:%S.%f'

class TestDatetimeTable(Base):
    """
       Example SQLAlchemy DB Model
       """
    # From the database, a library of event details are packaged together
    __tablename__ = 'test_datetime_table'
    # Columns
    id = Column(Integer, primary_key=True)
    datetime_str = Column(String(50), nullable=True)
    datetime_obj = Column(DateTime(), nullable=True)

    def __init__(self, datetime_str, datetime_obj):
        """
        Constructor for an event
        """

        self.datetime_str = datetime_str
        self.datetime_obj = datetime_obj

    @staticmethod
    def add_record(datetime_str=None, datetime_obj=None):
        if datetime_str is None:
            datetime_obj = datetime.now()

            print >> sys.stderr, "1111111111111111111111111111111111111111111111111"
            logger.debug("21111111111111111111111111111111111111111111111111")
            print >> sys.stderr, datetime_obj
            logger.debug(datetime_str)

            datetime_str = datetime_obj.strftime(DateTime_Format)

            print >> sys.stderr, "22222222222222222222222222222222222222222222222222"
            logger.debug("322222222222222222222222222222222222222222222222222")
            print >> sys.stderr, datetime_str
            logger.debug(datetime_str)

        session = SessionMaker()

        print >> sys.stderr, "3333333333333333333333333333333333333333333333333333"
        logger.debug("43333333333333333333333333333333333333333333333333333")
        print >> sys.stderr, datetime_str
        logger.debug(datetime_str)

        session.add(
            TestDatetimeTable(datetime_str=datetime_str, datetime_obj=datetime_obj))

        session.commit()
