import pandas as pd
import csv
def dictionary(path):

    csv_file_path = path+'.csv'

    # Initialize an empty dictionary
    data_dict = {}

    # Open the CSV file
    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.reader(file)

        # Read the first and second row
        headers = next(csv_reader)  # First row (keys)
        values = next(csv_reader)  # Second row (values)

        # Combine them into a dictionary
        data_dict = dict(zip(headers, values))

# Now 'data_dict' is a dictionary with the first row as keys and the second row as values
    return data_dict

def dictio():
    data = pd.read_csv('Attendance.csv')
    # Convert the DataFrame to a Dictionary
    data_dict = data.to_dict(orient='records')
    print(data_dict())



def one():
    data = dictio()
    print(data)
    for i in range(0, len(data)):
        print((data[i]))
    ref = 'ref'
    for i in range(0, len(data)):
        path = ref + str(i)
        path = db.collection('Attendance').document()
        path.set(data[i])
        print(path.id)
        print(path)





