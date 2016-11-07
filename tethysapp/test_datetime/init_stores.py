from .model import engine, Base, TestDatetimeTable


def init_test_datetime_db(first_time):
    Base.metadata.create_all(engine)
    # Put your persistent store initializer functions in here
    if first_time:
        TestDatetimeTable.add_record()
