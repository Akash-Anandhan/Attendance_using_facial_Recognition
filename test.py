import csv
import time
from datetime import datetime
with open('Attendance.csv','r+') as f:
    Data = f.readlines()
    name_list = []
    for line in Data:
        entry = line.split(',')
        name_list.append(entry[0])
with open('Attendance.csv', mode='r+', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    cur_datetime = datetime.now()
    date_time = cur_datetime.strftime('%H:%M:%S')
    t = time.strftime("%d-%m-%Y")# Skip header if present
    attendance_data = []
    for row in reader:
        if len(row) >= 2:  # Ensure there are at least two columns
            roll_number, date = row[0], row[1]  # Take only the first two columns
            attendance_data.append([roll_number, date])
        else:
            print(f"Skipping invalid row: {row}")  # Debugging message
    name = '10006'
    if name not in name_list:
        print('fresh attendance marked')
        f.writelines(f'\n{name},{t},{date_time},{"nil"}')
    else:
        x= True
        for i in range(0,len(attendance_data)):
            if name in attendance_data[i] and t in attendance_data[i]:
                print('your attendance for today is already marked')
                x= False
        if(x== True):
                print('new attendance marked')
                f.writelines(f'\n{name},{t},{date_time},{"nil"}')