from google.cloud import bigtable
import re
#client = bigtable.Client()

# For Table Manage
client = bigtable.Client(admin=True)

# For Read Only
#client = bigtable.Client(read_only=True)

#instances = client.list_instances()
instance = client.instance('autocomp','asia-east1-b')

#print(instance.list_tables()) # list of table object

#table = instance.table('new_test_teble')
#table.create()
#table.delete()

table = instance.list_tables()[0]
#column_families = table.list_column_families() #hash of column families

column_family_name = u'cf1'
column_name = b'pname'

row_key = 'sonywalkman'
cell_value = 'Sony Walkman'

for line in open('name.txt', 'r'):
    row_key = re.sub(r'[^a-zA-Z0-9]', '', line).lower()
    cell_value = re.sub(r'\"', '', line).rstrip('\n')
    print row_key
    print cell_value
    row = table.row(row_key)
    row.set_cell(column_family_name, column_name, cell_value)
    row.commit()
exit()

# ===== memo =====
#append a cell to a column


row_data = table.read_row(row_key)
if row_data is not None:
    print(row_data.cells[column_family_name][column_name][0].value)
else:
    print('row_data empyt')

#Delete cells in a row x column
#row.delete_cell(u'cf1', 'pname')
#row.commit()
