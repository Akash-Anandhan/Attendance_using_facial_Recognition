import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from PIL import Image, ImageTk
from Capture import record,logout
from dictionary import dictio,dictionary
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

db = firestore.client()
def map():
    data = dictio()
    print(data)
    for i in range(0, len(data)):
        print((data[i]))
    ref = 'ref'
    for i in range(0, len(data)):
        path = ref + 'i'
        path = db.collection('Attendance').document()
        std_ref = db.collection('Attendance').document()
        path.set(data[i])
        print(path.id)



name_dict = dictionary('student_data')

def update_attendance():
    with open('Attendance.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    tree.delete(*tree.get_children())

    # Insert new data from the CSV file into the Treeview
    for i, row in enumerate(data, 1):
        tree.insert('', 'end', values=(i,) + tuple(row))

    # Get the last added name
    last_added_name = data[-1][0] if data else ''

    # Update the label with the last added name
    name_label.config(text=format_student_details(name_dict[last_added_name], last_added_name))

    # Select the last row in the Treeview
    tree.selection_set(tree.get_children()[-1])

    # Load and display the image
    image_path = 'Training_Finding_encodings/faces/{}.jpg'.format(last_added_name) # Give the path to the images file
    image = Image.open(image_path)
    image = image.resize((300, 300))  # Adjust the size as per your requirements
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo, relief='solid', borderwidth=2)
    image_label.image = photo  # Keep a reference to prev
    messagebox.showinfo('information', 'Your Attendance is marked!\nPress key [esc] to return')

def detect_file_change():
    modified_time = os.path.getmtime('Attendance.csv')
    if modified_time > detect_file_change.last_modified_time:
        update_attendance()  # Update the attendance in the GUI
        detect_file_change.last_modified_time = modified_time
    clock.config(text=time.strftime("Date: %d-%m-%Y\nTime: %I:%M:%S"), background='light steel blue')
    window.after(1000, detect_file_change)

# Create the GUI window
window = tk.Tk()
window.title("Attendance Recording System")
window.geometry("1500x1000")
window['bg'] = 'light steel blue'

clock = tk.Label(window, background='white', foreground='black', font=('arial', 25, 'bold'), justify='left')
style = ttk.Style()
style.configure("Custom.Treeview", font=('Arial', 15))

# Create a Treeview widget
tree = ttk.Treeview(window, columns=('No.', 'Name', 'date','Intime','Out-time'), show='headings', style='Custom.Treeview')
name_label = tk.Label(window, font=('Arial', 25), background='deep sky blue', fg='black', justify='left',
                      relief='solid', borderwidth=5)
atten_name = tk.Label(window, text='Attendance System', font=('Arial', 20), fg='white',background='black', relief='solid', borderwidth=5)

# Create a label to display the image
def format_student_details(name, roll_no):
    formatted_text = "Name    : {}\n".format(name)
    formatted_text += "Roll No  : {}\n".format(roll_no)
    formatted_text += "Branch  : IT\n"
    formatted_text += "Section  : "
    return formatted_text

image_label = tk.Label(window, background='#34495e')

# Create a button to run the record() function
button = tk.Button(window, text="Capture-Login", command=record, background='green2', font=('Arial', 20, 'bold'),
                   fg='black', relief='solid', borderwidth=4)

button1 = tk.Button(window, text="Capture-logout", command=logout, background='green2', font=('Arial', 20, 'bold'),
                   fg='black', relief='solid', borderwidth=4)

button2 = tk.Button(window, text="Exit", command=map, background='green2', font=('Arial', 20, 'bold'),
                   fg='black', relief='solid', borderwidth=4)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Grid layout configuration
atten_name.grid(row=0, column=0, sticky='n', pady=20)
image_label.grid(row=0, column=0, padx=2, pady=0)
student_details_label = ttk.Label(window, text="Student Details:", font=('Arial', 15, 'bold'),
                                   padding=(10, 10), background='misty rose')
student_details_label.grid(row=0, column=0, padx=5, pady=2, sticky='s')
name_label.grid(row=1, column=0, padx=5, sticky='s')
tree.grid(row=0, column=1, sticky='ewns')

# Set row 1 weight to 1, so it takes the remaining vertical space
button.grid(row=2, column=0, padx=20, pady=20)
button1.grid(row=2, column=1, padx=20, pady=20)
button2.grid(row=2, column=2, padx=20, pady=20)

clock.grid(row=3, column=0, columnspan=3, padx=100, pady=3, sticky='w')

detect_file_change.last_modified_time = os.path.getmtime('Attendance.csv')

# Update the attendance initially
update_attendance()

# Start detecting file changes
detect_file_change()

# Start the GUI main loop
window.mainloop()





