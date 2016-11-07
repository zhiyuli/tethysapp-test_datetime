from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .model import engine, Base, TestDatetimeTable, SessionMaker, DateTime_Format
from datetime import datetime
import sys
import locale

@login_required()
def home(request):
    """
    Controller for the app home page.

    """
    print >>sys.stderr, "1122334112233411223341122334112233411223341122334112233411223341122334"

    locale_str = locale.getlocale()
    TestDatetimeTable.add_record()
    session = SessionMaker()
    all_records = session.query(TestDatetimeTable).all()
    status="success"
    status2 = "success"

    rec_list = []
    rec_list_2 = []
    rec_list_saved_obj = []
    rec_list_parsed_obj = []
    for rec in all_records:

        rec_list.append(rec.datetime_str)
        try:
            datetime_obj = datetime.strptime(rec.datetime_str, DateTime_Format)
            rec_list_2.append(str(datetime_obj))
        except Exception as ex:
            status = ex.message

        try:
            rec_list_saved_obj.append(rec.datetime_obj)
            rec_list_parsed_obj.append(rec.datetime_obj.strftime(DateTime_Format))
        except Exception as ex:
            status2 = ex.message

    print >>sys.stderr, rec_list
    context = {"rec_list": rec_list,
               "rec_list_2": rec_list_2,
               "rec_list_saved_obj": rec_list_saved_obj,
               "rec_list_parsed_obj": rec_list_parsed_obj,
               "status": status,
               "status2": status2,
               "locale_str": locale_str
               }

    return render(request, 'test_datetime/home.html', context)