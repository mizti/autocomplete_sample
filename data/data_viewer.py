from google.cloud import bigtable
import re
#client = bigtable.Client()

# For Table Manage
client = bigtable.Client(admin=True)
instance = client.instance('autocomp','asia-east1-b')
table = instance.list_tables()[0]

column_family_name = u'cf1'
column_name = b'pname'
row_key = 'zboosttriosohocellphonesignalboosterblack'

row_data = table.read_row(row_key)
print(row_data.__class__)
if row_data is not None:
    print(row_data.cells[column_family_name][column_name][0].value)
else:
    print('row_data empyt')

#Delete cells in a row x column
#row.delete_cell(u'cf1', 'pname')
#row.commit()
