from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .model import engine, Base, TestDatetimeTable, SessionMaker
from datetime import datetime
import sys

@login_required()
def home(request):
    """
    Controller for the app home page.

    """
    print >>sys.stderr, "1122334112233411223341122334112233411223341122334112233411223341122334"

  
    TestDatetimeTable.add_record()
    session = SessionMaker()
    all_records = session.query(TestDatetimeTable).all()

    rec_list = []
    rec_list_2 = []
    for rec in all_records:
        rec_list.append(rec.datetime_str)
        datetime_obj = datetime.strptime(rec.datetime_str, '%Y-%m-%dT%X.%f')
        rec_list_2.append(str(datetime_obj))

    print >> sys.stderr, rec_list
    context = {"rec_list": rec_list, "rec_list_2": rec_list_2}

    return render(request, 'test_datetime/home.html', context)