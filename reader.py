import sys
from classes import CSVHandler, PICKLEHandler, JSONHandler, ls

file_in = sys.argv[1]
file_out = sys.argv[2]
location_x = int(sys.argv[3])
location_y = int(sys.argv[4])
command_change = sys.argv[5]

pickle_file = PICKLEHandler(file_in, file_out)
json_file = JSONHandler(file_in, file_out)
csv_file = CSVHandler(file_in, file_out)

if file_in[-3:] == 'csv':
    csv_file.load_file()
elif file_in[-4:] == 'json':
    json_file.load_file('')
elif file_in[-6:] == 'pickle':
    pickle_file.load_file('b')
else:
    print("Wrong file type selected.")

ls[location_x][location_y] = command_change
print(ls)

if file_out[-3:] == 'csv':
    csv_file.dump_file()
elif file_out[-4:] == 'json':
    json_file.dump_file('')
elif file_out[-6:] == 'pickle':
    pickle_file.dump_file('b')
else:
    print("Wrong file type selected.")
