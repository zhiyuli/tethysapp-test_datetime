# Put your persistent store models in this file
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

from .app import TestDatetime

from datetime import datetime
import logging
logger = logging.getLogger(__name__)

engine = TestDatetime.get_persistent_store_engine('test_datetime_db_engine')
SessionMaker = sessionmaker(bind=engine)
Base = declarative_base()


class TestDatetimeTable(Base):
    """
       Example SQLAlchemy DB Model
       """
    # From the database, a library of event details are packaged together
    __tablename__ = 'test_datetime_table'
    # Columns
    id = Column(Integer, primary_key=True)
    datetime_str = Column(String(50), nullable=True)

    def __init__(self, datetime_str):
        """
        Constructor for an event
        """

        self.datetime_str = datetime_str

    @staticmethod
    def add_record(datetime_str=None):
        if datetime_str is None:
            now_obj = datetime.now()

            print >> sys.stderr, "1111111111111111111111111111111111111111111111111"
            logger.debug("21111111111111111111111111111111111111111111111111")
            print >> sys.stderr, now_obj
            logger.debug(datetime_str)

            datetime_str = now_obj.strftime('%Y-%m-%dT%X.%f')

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
            TestDatetimeTable(datetime_str=datetime_str))
        session.commit()
