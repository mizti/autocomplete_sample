from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from google.cloud import bigtable
from google.cloud.bigtable.row_filters import RowKeyRegexFilter

def index(request):
    return HttpResponse("designate some characters")

def suggest(request, input_value):
    print(input_value)
    #return HttpResponse("['indian curry']")
    #listed = ["serval", "hoge", "india", "bag"]
    listed_items = get_data(input_value)
    #listed = [
    #    value + "77",
    #    value + "78",
    #    value + "79"
    #]
    ret = json.dumps(listed_items)
    print(ret)
    return HttpResponse(ret)



client = bigtable.Client(admin=True)
instance = client.instance('autocomp','asia-east1-b')
table = instance.list_tables()[0]

# For Table Manage
def get_data(row_key):
    #client = bigtable.Client(admin=True)
    #instance = client.instance('autocomp','asia-east1-b')
    #table = instance.list_tables()[0]

    column_family_name = u'cf1'
    column_name = b'pname'
    #filt = RowKeyRegexFilter(b'.+')
    filt = RowKeyRegexFilter(b'.+') # can be enhanced
    #filt = RowKeyRegexFilter(b'.+') # can be enhanced
    row_data = table.read_rows(start_key=row_key,limit=5,filter_=filt)
    row_data.consume_all()
    rows = row_data.rows
    ret = []
    for row in rows:
        ret.append(rows[row].cells[column_family_name][column_name][0].value)
    return sorted(ret)

    row_data = table.read_row(row_key)
    if row_data is not None:
        value = row_data.cells[column_family_name][column_name][0].value
        print(value)
        return value
    else:
        print('row_data empty')
        return ''

#Delete cells in a row x column
#row.delete_cell(u'cf1', 'pname')
#row.commit()
