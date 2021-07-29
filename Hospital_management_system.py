import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='mayank123',
    database='Hospital_management'
)
my_cursor = my_db.cursor()


def show_frame(frame):
    place = 0
    while place != 16:
        frame.tkraise()
        place += 1


def add_appointment():
    appointment_number = appointment_no_input.get()
    patient_id = patient_id_input_aa.get()
    doctor = doctor_input.get()
    problem = problem_input.get()
    time = time_input.get()
    date = date_input.get()
    base = "INSERT INTO appointment VALUES(%s, %s, %s, %s, %s, %s)"
    value = (appointment_number, patient_id, doctor, problem, time, date)
    my_cursor.execute(base, value)
    my_db.commit()
    messagebox.showinfo("Done!", "Appointment Added!!")
    patient_id_input_aa.delete(0, 'end')
    appointment_no_input.delete(0, 'end')
    doctor_input.delete(0, 'end')
    problem_input.delete(0, 'end')
    time_input.delete(0, 'end')
    date_input.delete(0, 'end')


def remove_medication_fnc():
    medicine_no = medicine_input.get()
    medicine_no = (medicine_no,)
    base = "DELETE FROM medication WHERE medicine_id = %s"
    my_cursor.execute(base, medicine_no)
    my_db.commit()
    messagebox.showinfo("Removed!", "Medicine Removed!!")
    medicine_input.delete(0, 'end')


def remove_appointment():
    appointment_number = appointment_number_input.get()
    appointment_number = (appointment_number,)
    base = 'DELETE FROM appointment WHERE appointment_no = %s'
    my_cursor.execute(base, appointment_number)
    my_db.commit()
    messagebox.showinfo("Removed!", "Appointment Remove!!")
    appointment_number_input.delete(0, 'end')


def add_patient():
    patient_id = patient_id_input_ap.get()
    name = patient_name_input.get()
    gender = gender_input.get()
    age = age_input.get()
    address = address_input.get()
    phone_no = phone_no_input.get()
    base = "INSERT INTO patients VALUES(%s, %s, %s, %s, %s, %s)"
    value = (patient_id, name, gender, int(age), address, int(phone_no))
    my_cursor.execute(base, value)
    my_db.commit()
    messagebox.showinfo("Done!", "Patient Added!!")
    patient_id_input_ap.delete(0, 'end')
    patient_name_input.delete(0, 'end')
    gender_input.delete(0, 'end')
    age_input.delete(0, 'end')
    address_input.delete(0, 'end')
    phone_no_input.delete(0, 'end')


def remove_patient():
    patient_id = patient_id_input.get()
    patient_id = (patient_id,)
    base = 'DELETE FROM patients WHERE patient_id = %s'
    my_cursor.execute(base, patient_id)
    my_db.commit()
    messagebox.showinfo("Remove!", "Patient Record Remove!!")
    patient_id_input.delete(0, 'end')


def add_medication_fuc():
    medicine_no = medicine_no_input.get()
    name = medicine_name_input.get()
    medicine_brand = medicine_brand_input.get()
    dec = medicine_description_input.get()
    base = "INSERT INTO medication VALUES(%s, %s, %s, %s)"
    value = (medicine_no, name, medicine_brand, dec)
    my_cursor.execute(base, value)
    my_db.commit()
    messagebox.showinfo("Done!", "Medication Added!!")
    medicine_no_input.delete(0, 'end')
    medicine_name_input.delete(0, 'end')
    medicine_brand_input.delete(0, 'end')
    medicine_description_input.delete(0, 'end')


def room_show_records():
    show_frame(room_frame)
    for child in rooms_treeview.get_children():
        rooms_treeview.delete(child)
    count = 0
    my_db.commit()
    my_cursor.execute('select * from rooms')
    result = my_cursor.fetchall()

    for record in result:
        if count % 2 == 0:
            rooms_treeview.insert(parent='', index='end', text="",
                                  values=(record[0], record[1], record[2], record[3]),
                                  tags=('even_row',))
        else:
            rooms_treeview.insert(parent='', index='end', text="",
                                  values=(record[0], record[1], record[2], record[3]),
                                  tags=('odd_row',))
        count += 1


def appointment_show_records():
    show_frame(check_appointment_frame)
    for child in appointment_treeview.get_children():
        appointment_treeview.delete(child)
    count = 0
    my_db.commit()
    my_cursor.execute('select * from appointment')
    result = my_cursor.fetchall()
    for record in result:
        if count % 2 == 0:
            appointment_treeview.insert(parent='', index='end', text="",
                                        values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                                        tags=('even_row',))
        else:
            appointment_treeview.insert(parent='', index='end', text="",
                                        values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                                        tags=('odd_row',))
        count += 1


def show_medication_fnc():
    show_frame(check_medication_frame)
    for child in medication_treeview.get_children():
        medication_treeview.delete(child)
    count = 0
    my_db.commit()
    my_cursor.execute('select * from medication')
    result = my_cursor.fetchall()
    for record in result:
        if count % 2 == 0:
            medication_treeview.insert(parent='', index='end', text="",
                                       values=(record[0], record[1], record[2], record[3]),
                                       tags=('even_row',))
        else:
            medication_treeview.insert(parent='', index='end', text="",
                                       values=(record[0], record[1], record[2], record[3]),
                                       tags=('odd_row',))
        count += 1


def show_patient_fnc():
    show_frame(check_patient_frame)
    for child in patient_treeview.get_children():
        patient_treeview.delete(child)
    count = 0
    my_db.commit()
    my_cursor.execute('select * from patients')
    result = my_cursor.fetchall()
    for record in result:
        if count % 2 == 0:
            patient_treeview.insert(parent='', index='end', text="",
                                    values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                                    tags=('even_row',))
        else:
            patient_treeview.insert(parent='', index='end', text="",
                                    values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                                    tags=('odd_row',))
        count += 1


def show_doctor():
    show_frame(doctor_frame)
    for child in doctor_treeview.get_children():
        doctor_treeview.delete(child)
    count = 0
    my_db.commit()
    my_cursor.execute('select * from doctor')
    result = my_cursor.fetchall()
    for record in result:
        if count % 2 == 0:
            doctor_treeview.insert(parent='', index='end', text="",
                                   values=(record[0], record[1], record[2], record[3]),
                                   tags=('even_row',))
        else:
            doctor_treeview.insert(parent='', index='end', text="",
                                   values=(record[0], record[1], record[2], record[3]),
                                   tags=('odd_row',))
        count += 1


def open_report():
    report = filedialog.askopenfilename(initialdir="/report",
                                        title="Open Report", filetypes=(("Text Files", "*.txt"),))
    print(report)
    global current_report, new_file
    new_file = False
    current_report = report
    report = open(report, "r")
    work_page.delete(1.0, tk.END)
    work_page.insert(tk.END, report.read())


def new_file_f(report):
    global new_file, current_report
    new_file = False
    current_report = report


def save_report():
    if new_file:
        report = filedialog.asksaveasfilename(initialdir="/report")
        new_file_f(report)
        report = open(report, "w")
        report.write(work_page.get(1.0, tk.END))

    else:
        report = open(current_report, 'w')
        report.write(work_page.get(1.0, tk.END))


def create_report():
    work_page.delete(1.0, tk.END)
    global new_file
    new_file = True


window = tk.Tk()
window.geometry('700x450')
window.title("Hospital Management")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
icon = tk.PhotoImage(file="images/icon.png")
window.iconphoto(False, icon)

# Images Intro
original = Image.open('images/Patient_button.png')
resize = original.resize((193, 177), Image.ANTIALIAS)
patient_button_img = ImageTk.PhotoImage(resize)

original = Image.open('images/appointment_button.png')
resize = original.resize((193, 177), Image.ANTIALIAS)
appointment_button_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Doctors_button.png')
resize = original.resize((193, 177), Image.ANTIALIAS)
doctors_button_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Rooms_button.png')
resize = original.resize((193, 177), Image.ANTIALIAS)
rooms_button_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Medication_button.png')
resize = original.resize((193, 177), Image.ANTIALIAS)
medication_button_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Report_image.png')
resize = original.resize((193, 177), Image.ANTIALIAS)
report_button_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Back_button.png')
resize = original.resize((52, 41), Image.ANTIALIAS)
back_button_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Add_button.png')
resize = original.resize((106, 45), Image.ANTIALIAS)
add_button_img = ImageTk.PhotoImage(resize)

original = Image.open('images/remove_button.png')
resize = original.resize((176, 45), Image.ANTIALIAS)
remove_button_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Add_patient_records_button.png')
resize = original.resize((350, 110), Image.ANTIALIAS)
add_patient_button_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Check_patient_records_button.png')
resize = original.resize((350, 110), Image.ANTIALIAS)
check_patient_button_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Remove_patient_records_button.png')
resize = original.resize((350, 110), Image.ANTIALIAS)
remove_patient_button_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Add_patient_records_frame.png')
resize = original.resize((700, 450), Image.ANTIALIAS)
add_patient_frame_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Remove_patient_records_frame.png')
resize = original.resize((700, 450), Image.ANTIALIAS)
remove_patient_frame_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Add_appointment_button.png')
resize = original.resize((300, 110), Image.ANTIALIAS)
add_appointment_button_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Check_appointment_button.png')
resize = original.resize((300, 110), Image.ANTIALIAS)
check_appointment_button_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Remove_appointment_button.png')
resize = original.resize((300, 110), Image.ANTIALIAS)
remove_appointment_button_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Add_appointment_frame.png')
resize = original.resize((700, 450), Image.ANTIALIAS)
add_appointment_frame_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Remove_appointment_frame.png')
resize = original.resize((700, 450), Image.ANTIALIAS)
remove_appointment_frame_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Add_medication_button.png')
resize = original.resize((300, 110), Image.ANTIALIAS)
add_medication_button_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Check_medication_button.png')
resize = original.resize((300, 110), Image.ANTIALIAS)
check_medication_button_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Remove_medication_button.png')
resize = original.resize((300, 110), Image.ANTIALIAS)
remove_medication_button_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Add_medication_frame.png')
resize = original.resize((700, 450), Image.ANTIALIAS)
add_medication_frame_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Remove_medication_frame.png')
resize = original.resize((700, 450), Image.ANTIALIAS)
remove_medication_frame_img = ImageTk.PhotoImage(resize)

original = Image.open('images/Open_rp_image.png')
resize = original.resize((185, 45), Image.ANTIALIAS)
open_rp = ImageTk.PhotoImage(resize)

original = Image.open('images/Create_rp_image.png')
resize = original.resize((203, 45), Image.ANTIALIAS)
create_rp = ImageTk.PhotoImage(resize)

original = Image.open('images/save_image.png')
resize = original.resize((84, 45), Image.ANTIALIAS)
save_rp = ImageTk.PhotoImage(resize)

# Frames
appointment_sub_frame = tk.Frame(master=window, bg='white', width=700, height=450)
appointment_sub_frame.grid(row=0, column=0, sticky='nsew')

report_frame = tk.Frame(master=window, bg='white', width=700, height=450)
report_frame.grid(row=0, column=0, sticky='nsew')

patient_sub_frame = tk.Frame(master=window, bg='white', width=700, height=450)
patient_sub_frame.grid(row=0, column=0, sticky='nsew')

doctor_frame = tk.Frame(master=window, bg='white', width=700, height=450)
doctor_frame.grid(row=0, column=0, sticky='nsew')

medication_sub_frame = tk.Frame(master=window, bg='white', width=700, height=450)
medication_sub_frame.grid(row=0, column=0, sticky='nsew')

room_frame = tk.Frame(master=window, bg='white', width=700, height=450)
room_frame.grid(row=0, column=0, sticky='nsew')

remove_patient_frame = tk.Frame(master=window, bg='white', width=700, height=450)
remove_patient_frame.grid(row=0, column=0, sticky='nsew')

add_patient_frame = tk.Frame(master=window, bg='white', width=700, height=450)
add_patient_frame.grid(row=0, column=0, sticky='nsew')

check_patient_frame = tk.Frame(master=window, bg='white', width=700, height=450)
check_patient_frame.grid(row=0, column=0, sticky='nsew')

remove_appointment_frame = tk.Frame(master=window, bg='white', width=700, height=450)
remove_appointment_frame.grid(row=0, column=0, sticky='nsew')

add_appointment_frame = tk.Frame(master=window, bg='white', width=700, height=450)
add_appointment_frame.grid(row=0, column=0, sticky='nsew')

check_appointment_frame = tk.Frame(master=window, bg='white', width=700, height=450)
check_appointment_frame.grid(row=0, column=0, sticky='nsew')

remove_medication_frame = tk.Frame(master=window, bg='white', width=700, height=450)
remove_medication_frame.grid(row=0, column=0, sticky='nsew')

add_medication_frame = tk.Frame(master=window, bg='white', width=700, height=450)
add_medication_frame.grid(row=0, column=0, sticky='nsew')

check_medication_frame = tk.Frame(master=window, bg='white', width=700, height=450)
check_medication_frame.grid(row=0, column=0, sticky='nsew')

main_frame = tk.Frame(master=window, bg='white', width=700, height=450)
main_frame.grid(row=0, column=0, sticky='nsew')

# Main Menu items
appointment_button = tk.Button(master=main_frame,
                               image=appointment_button_img,
                               borderwidth=0,
                               command=lambda: show_frame(appointment_sub_frame))
Patient_button = tk.Button(master=main_frame,
                           image=patient_button_img,
                           borderwidth=0,
                           command=lambda: show_frame(patient_sub_frame))
Doctors_button = tk.Button(master=main_frame,
                           image=doctors_button_img,
                           borderwidth=0,
                           command=lambda: show_doctor())
Rooms_button = tk.Button(master=main_frame,
                         image=rooms_button_img,
                         borderwidth=0,
                         command=lambda: room_show_records())
Medication_button = tk.Button(master=main_frame,
                              image=medication_button_img,
                              borderwidth=0,
                              command=lambda: show_frame(medication_sub_frame))
Report_button = tk.Button(master=main_frame,
                          image=report_button_img,
                          borderwidth=0,
                          command=lambda: show_frame(report_frame))

# Main Menu Alignments
appointment_button.place(x=35, y=35)
Patient_button.place(x=253.5, y=35)
Doctors_button.place(x=472, y=35)
Rooms_button.place(x=35, y=237.5)
Medication_button.place(x=253, y=237.5)
Report_button.place(x=472, y=237.5)

# Appointment Sub items

add_appointment_button = tk.Button(master=appointment_sub_frame,
                                   image=add_appointment_button_img,
                                   borderwidth=0,
                                   command=lambda: show_frame(add_appointment_frame))

check_appointment_button = tk.Button(master=appointment_sub_frame,
                                     image=check_appointment_button_img,
                                     borderwidth=0,
                                     command=lambda: appointment_show_records())

remove_appointment_button = tk.Button(master=appointment_sub_frame,
                                      image=remove_appointment_button_img,
                                      borderwidth=0,
                                      command=lambda: show_frame(remove_appointment_frame))

back_button_1 = tk.Button(master=appointment_sub_frame,
                          image=back_button_img,
                          borderwidth=0,
                          command=lambda: show_frame(main_frame))

# Appointment Sub items Alignments
add_appointment_button.place(x=200, y=35)
check_appointment_button.place(x=200, y=170)
remove_appointment_button.place(x=200, y=305)
back_button_1.place(x=20, y=20)

# Add appointment items
bg1 = tk.Label(master=add_appointment_frame,
               image=add_appointment_frame_img)

back_button_2 = tk.Button(master=add_appointment_frame,
                          image=back_button_img,
                          borderwidth=0,
                          command=lambda: show_frame(appointment_sub_frame))

add_button_1 = tk.Button(master=add_appointment_frame,
                         borderwidth=0,
                         image=add_button_img, command=lambda: add_appointment())

appointment_no_input = tk.Entry(master=add_appointment_frame, bg="#EEEEEE", highlightbackground="#07A9CF",
                                highlightcolor="#07A9CF")

patient_id_input_aa = tk.Entry(master=add_appointment_frame, bg="#EEEEEE", highlightbackground="#07A9CF",
                               highlightcolor="#07A9CF")

doctor_input = tk.Entry(master=add_appointment_frame, bg="#EEEEEE", highlightbackground="#07A9CF",
                        highlightcolor="#07A9CF")

problem_input = tk.Entry(master=add_appointment_frame, bg="#EEEEEE", highlightbackground="#07A9CF",
                         highlightcolor="#07A9CF")

time_input = tk.Entry(master=add_appointment_frame, bg="#EEEEEE", highlightbackground="#07A9CF",
                      highlightcolor="#07A9CF")

date_input = tk.Entry(master=add_appointment_frame, bg="#EEEEEE", highlightbackground="#07A9CF",
                      highlightcolor="#07A9CF")

# Add appointment items alignment
bg1.pack()
back_button_2.place(x=20, y=20)
add_button_1.place(x=297, y=370)
appointment_no_input.place(x=350, y=104)
patient_id_input_aa.place(x=350, y=147)
doctor_input.place(x=350, y=189)
problem_input.place(x=350, y=232)
time_input.place(x=350, y=274)
date_input.place(x=350, y=316)

# Remove Appointment items
bg2 = tk.Label(master=remove_appointment_frame, image=remove_appointment_frame_img)

back_button_3 = tk.Button(master=remove_appointment_frame, image=back_button_img,
                          command=lambda: show_frame(appointment_sub_frame), borderwidth=0)

appointment_number_input = tk.Entry(master=remove_appointment_frame, bg="#EEEEEE", highlightbackground="#07A9CF",
                                    highlightcolor="#07A9CF")

remove_button_1 = tk.Button(master=remove_appointment_frame, image=remove_button_img, borderwidth=0,
                            command=lambda: remove_appointment())

# Remove Appointment items alignments
bg2.pack()
back_button_3.place(x=20, y=20)
appointment_number_input.place(x=350, y=210)
remove_button_1.place(x=262, y=370)

# Check  Appointment Items
back_button_4 = tk.Button(master=check_appointment_frame, image=back_button_img,
                          command=lambda: show_frame(appointment_sub_frame), borderwidth=0)

appointment_treeview_frame = tk.Frame(master=check_appointment_frame, background='#07A9CF')

appointment_treeview = ttk.Treeview(appointment_treeview_frame, height=17)

appointment_treeview['columns'] = ("Appointment No", "Patient Id", "Doctor Id", "Problem", "Time", "Date")

appointment_treeview.column("#0", width=0, stretch=tk.NO)
appointment_treeview.column("Appointment No", anchor=tk.CENTER, width=84)
appointment_treeview.column("Patient Id", anchor=tk.CENTER, width=84)
appointment_treeview.column("Doctor Id", anchor=tk.CENTER, width=84)
appointment_treeview.column("Problem", anchor=tk.W, width=88)
appointment_treeview.column("Time", anchor=tk.CENTER, width=80)
appointment_treeview.column("Date", anchor=tk.CENTER, width=84)

appointment_treeview.heading("#0", text="", anchor=tk.W)
appointment_treeview.heading("Appointment No", text="Appointment No", anchor=tk.CENTER)
appointment_treeview.heading("Patient Id", text="Patient Id", anchor=tk.CENTER)
appointment_treeview.heading("Doctor Id", text="Doctor Id", anchor=tk.CENTER)
appointment_treeview.heading("Problem", text="Problem", anchor=tk.CENTER)
appointment_treeview.heading("Time", text="Time", anchor=tk.CENTER)
appointment_treeview.heading("Date", text="Date", anchor=tk.CENTER)

appointment_treeview.tag_configure('odd_row', background='white')
appointment_treeview.tag_configure('even_row', background='#E5E5E5')

# Check Appointment Items alignments
back_button_4.place(x=20, y=20)
appointment_treeview.pack(padx=3, pady=3)
appointment_treeview_frame.place(x=96, y=50)

# Rooms items
back_button_5 = tk.Button(master=room_frame, image=back_button_img,
                          command=lambda: show_frame(main_frame), borderwidth=0)
rooms_treeview_frame = tk.Frame(master=room_frame, background='#07A9CF')

rooms_treeview = ttk.Treeview(rooms_treeview_frame, height=17)

rooms_treeview['columns'] = ("Room Number", "Status", "Floor", "Patient Id")

rooms_treeview.column("#0", width=0, stretch=tk.NO)
rooms_treeview.column("Room Number", anchor=tk.CENTER, width=126)
rooms_treeview.column("Status", anchor=tk.CENTER, width=126)
rooms_treeview.column("Floor", anchor=tk.CENTER, width=126)
rooms_treeview.column("Patient Id", anchor=tk.W, width=126)

rooms_treeview.heading("#0", text="", anchor=tk.W)
rooms_treeview.heading("Room Number", text="Room Number", anchor=tk.CENTER)
rooms_treeview.heading("Status", text="Status", anchor=tk.CENTER)
rooms_treeview.heading("Floor", text="Floor", anchor=tk.CENTER)
rooms_treeview.heading("Patient Id", text="Patient Id", anchor=tk.CENTER)

rooms_treeview.tag_configure('odd_row', background='white')
rooms_treeview.tag_configure('even_row', background='#E5E5E5')

# Rooms item alignments
back_button_5.place(x=20, y=20)
rooms_treeview.pack(padx=3, pady=3)
rooms_treeview_frame.place(x=96, y=50)

# Patient Sub items
back_button_6 = tk.Button(master=patient_sub_frame, image=back_button_img,
                          command=lambda: show_frame(main_frame), borderwidth=0)

add_patient_button = tk.Button(master=patient_sub_frame, image=add_patient_button_img,
                               command=lambda: show_frame(add_patient_frame), borderwidth=0)

check_patient_button = tk.Button(master=patient_sub_frame, image=check_patient_button_img,
                                 command=lambda: show_patient_fnc(), borderwidth=0)

remove_patient_button = tk.Button(master=patient_sub_frame, image=remove_patient_button_img,
                                  command=lambda: show_frame(remove_patient_frame), borderwidth=0)

# Patient sub items alignment
back_button_6.place(x=20, y=20)
add_patient_button.place(x=175, y=35)
check_patient_button.place(x=175, y=170)
remove_patient_button.place(x=175, y=305)

# Add patient items
bg3 = tk.Label(master=add_patient_frame, image=add_patient_frame_img)

back_button_7 = tk.Button(master=add_patient_frame, image=back_button_img,
                          command=lambda: show_frame(patient_sub_frame), borderwidth=0)

patient_id_input_ap = tk.Entry(master=add_patient_frame, bg="#EEEEEE", highlightbackground="#07A9CF",
                               highlightcolor="#07A9CF")

patient_name_input = tk.Entry(master=add_patient_frame, bg="#EEEEEE", highlightbackground="#07A9CF",
                              highlightcolor="#07A9CF")

gender_input = tk.Entry(master=add_patient_frame, bg="#EEEEEE", highlightbackground="#07A9CF",
                        highlightcolor="#07A9CF")

age_input = tk.Entry(master=add_patient_frame, bg="#EEEEEE", highlightbackground="#07A9CF",
                     highlightcolor="#07A9CF")

address_input = tk.Entry(master=add_patient_frame, bg="#EEEEEE", highlightbackground="#07A9CF",
                         highlightcolor="#07A9CF")

phone_no_input = tk.Entry(master=add_patient_frame, bg="#EEEEEE", highlightbackground="#07A9CF",
                          highlightcolor="#07A9CF")

add_button_2 = tk.Button(master=add_patient_frame, image=add_button_img,
                         borderwidth=0, command=lambda: add_patient())

# Add Patient items alignments
bg3.pack()
back_button_7.place(x=20, y=20)
patient_id_input_ap.place(x=350, y=101)
patient_name_input.place(x=350, y=147)
gender_input.place(x=350, y=189)
age_input.place(x=350, y=232)
address_input.place(x=350, y=274)
phone_no_input.place(x=350, y=317)
add_button_2.place(x=297, y=370)

# Remove Patient items
bg4 = tk.Label(master=remove_patient_frame, image=remove_patient_frame_img)

patient_id_input = tk.Entry(master=remove_patient_frame, bg="#EEEEEE", highlightbackground="#07A9CF",
                            highlightcolor="#07A9CF")

back_button_8 = tk.Button(master=remove_patient_frame, image=back_button_img,
                          command=lambda: show_frame(patient_sub_frame), borderwidth=0)

remove_button_2 = tk.Button(master=remove_patient_frame, image=remove_button_img,
                            borderwidth=0, command=lambda: remove_patient())

# Remove Patient items alignments
bg4.pack()
patient_id_input.place(x=350, y=210)
back_button_8.place(x=20, y=20)
remove_button_2.place(x=262, y=370)

# Check Patient items
back_button_9 = tk.Button(master=check_patient_frame, image=back_button_img,
                          command=lambda: show_frame(patient_sub_frame), borderwidth=0)

patient_treeview_frame = tk.Frame(master=check_patient_frame, background='#07A9CF')

patient_treeview = ttk.Treeview(patient_treeview_frame, height=17)

patient_treeview['columns'] = ("Patient Id", "Name", "Gender", "Age", "Address", "Phone No")

patient_treeview.column("#0", width=0, stretch=tk.NO)
patient_treeview.column("Patient Id", anchor=tk.CENTER, width=108)
patient_treeview.column("Name", anchor=tk.CENTER, width=84)
patient_treeview.column("Gender", anchor=tk.CENTER, width=84)
patient_treeview.column("Age", anchor=tk.W, width=60)
patient_treeview.column("Address", anchor=tk.W, width=84)
patient_treeview.column("Phone No", anchor=tk.W, width=84)

patient_treeview.heading("#0", text="", anchor=tk.W)
patient_treeview.heading("Patient Id", text="Patient Id", anchor=tk.CENTER)
patient_treeview.heading("Name", text="Name", anchor=tk.CENTER)
patient_treeview.heading("Gender", text="Gender", anchor=tk.CENTER)
patient_treeview.heading("Age", text="Age", anchor=tk.CENTER)
patient_treeview.heading("Address", text="Address", anchor=tk.CENTER)
patient_treeview.heading("Phone No", text="Phone No", anchor=tk.CENTER)

patient_treeview.tag_configure('odd_row', background='white')
patient_treeview.tag_configure('even_row', background='#E5E5E5')

# Check Patient items alignment
back_button_9.place(x=20, y=20)
patient_treeview.pack(padx=3, pady=3)
patient_treeview_frame.place(x=96, y=50)

# Medication sub items
back_button_10 = tk.Button(master=medication_sub_frame, image=back_button_img,
                           command=lambda: show_frame(main_frame), borderwidth=0)

add_medication = tk.Button(master=medication_sub_frame, image=add_medication_button_img,
                           command=lambda: show_frame(add_medication_frame), borderwidth=0)

check_medication = tk.Button(master=medication_sub_frame, image=check_medication_button_img,
                             command=lambda: show_medication_fnc(), borderwidth=0)

remove_medication = tk.Button(master=medication_sub_frame, image=remove_medication_button_img,
                              command=lambda: show_frame(remove_medication_frame), borderwidth=0)

# Medication sub items alignments
back_button_10.place(x=20, y=20)
add_medication.place(x=200, y=35)
check_medication.place(x=200, y=170)
remove_medication.place(x=200, y=305)

# Add medication items
bg5 = tk.Label(master=add_medication_frame, image=add_medication_frame_img)
back_button_11 = tk.Button(master=add_medication_frame, image=back_button_img,
                           command=lambda: show_frame(medication_sub_frame), borderwidth=0)
medicine_no_input = tk.Entry(master=add_medication_frame, bg="#EEEEEE", highlightbackground="#07A9CF",
                             highlightcolor="#07A9CF")
medicine_name_input = tk.Entry(master=add_medication_frame, bg="#EEEEEE", highlightbackground="#07A9CF",
                               highlightcolor="#07A9CF")
medicine_brand_input = tk.Entry(master=add_medication_frame, bg="#EEEEEE", highlightbackground="#07A9CF",
                                highlightcolor="#07A9CF")
medicine_description_input = tk.Entry(master=add_medication_frame, bg="#EEEEEE", highlightbackground="#07A9CF",
                                      highlightcolor="#07A9CF")
add_button_3 = tk.Button(master=add_medication_frame, image=add_button_img,
                         borderwidth=0, command=lambda: add_medication_fuc())

# Add medication items alignment
bg5.pack()
back_button_11.place(x=20, y=20)
add_button_3.place(x=297, y=370)
medicine_no_input.place(x=350, y=121)
medicine_name_input.place(x=350, y=178)
medicine_brand_input.place(x=350, y=234)
medicine_description_input.place(x=350, y=291)

# Check Medication Items
back_button_12 = tk.Button(master=check_medication_frame, image=back_button_img,
                           command=lambda: show_frame(medication_sub_frame), borderwidth=0)

medication_treeview_frame = tk.Frame(master=check_medication_frame, background='#07A9CF')

medication_treeview = ttk.Treeview(medication_treeview_frame, height=17)

medication_treeview['columns'] = ("Medicine No", "Name", "Brand", "Description")

medication_treeview.column("#0", width=0, stretch=tk.NO)
medication_treeview.column("Medicine No", anchor=tk.CENTER, width=120)
medication_treeview.column("Name", anchor=tk.CENTER, width=120)
medication_treeview.column("Brand", anchor=tk.CENTER, width=80)
medication_treeview.column("Description", anchor=tk.W, width=184)

medication_treeview.heading("#0", text="", anchor=tk.W)
medication_treeview.heading("Medicine No", text="Medicine No", anchor=tk.CENTER)
medication_treeview.heading("Name", text="Name", anchor=tk.CENTER)
medication_treeview.heading("Brand", text="Brand", anchor=tk.CENTER)
medication_treeview.heading("Description", text="Description", anchor=tk.CENTER)

medication_treeview.tag_configure('odd_row', background='white')
medication_treeview.tag_configure('even_row', background='#E5E5E5')

# Check Medication Items Alignments
back_button_12.place(x=20, y=20)
medication_treeview.pack(padx=3, pady=3)
medication_treeview_frame.place(x=96, y=50)

# Remove Medication Items
bg6 = tk.Label(master=remove_medication_frame, image=remove_medication_frame_img)
back_button_13 = tk.Button(master=remove_medication_frame, image=back_button_img,
                           command=lambda: show_frame(medication_sub_frame), borderwidth=0)

medicine_input = tk.Entry(master=remove_medication_frame, bg="#EEEEEE", highlightbackground="#07A9CF",
                          highlightcolor="#07A9CF")
remove_button_3 = tk.Button(master=remove_medication_frame, image=remove_button_img,
                            borderwidth=0, command=lambda: remove_medication_fnc())

# Remove Medication Items Alignments
bg6.pack()
back_button_13.place(x=20, y=20)
medicine_input.place(x=350, y=210)
remove_button_3.place(x=262, y=370)

# Report items
new_file = True
current_report = ''
back_button_14 = tk.Button(master=report_frame, image=back_button_img,
                           command=lambda: show_frame(main_frame), borderwidth=0)
open_rp_button = tk.Button(master=report_frame, image=open_rp, borderwidth=0, command=lambda: open_report())
save_rp_button = tk.Button(master=report_frame, image=save_rp, borderwidth=0, command=lambda: save_report())
create_rp_button = tk.Button(master=report_frame, image=create_rp, borderwidth=0, command=lambda: create_report())
work_page = tk.Text(master=report_frame, width=75, height=23)

# Report items alignments
back_button_14.place(x=20, y=20)
open_rp_button.place(x=452, y=385)
save_rp_button.place(x=308, y=385)
create_rp_button.place(x=45, y=385)
work_page.place(x=80, y=40)

# doctor items
back_button_15 = tk.Button(master=doctor_frame, image=back_button_img,
                           command=lambda: show_frame(main_frame), borderwidth=0)
doctor_treeview_frame = tk.Frame(master=doctor_frame, background='#07A9CF')

doctor_treeview = ttk.Treeview(doctor_treeview_frame, height=17)

doctor_treeview['columns'] = ("Doctor Id", "Department", "Status", "Floor")

doctor_treeview.column("#0", width=0, stretch=tk.NO)
doctor_treeview.column("Doctor Id", anchor=tk.CENTER, width=126)
doctor_treeview.column("Department", anchor=tk.CENTER, width=126)
doctor_treeview.column("Status", anchor=tk.CENTER, width=126)
doctor_treeview.column("Floor", anchor=tk.CENTER, width=126)

doctor_treeview.heading("#0", text="", anchor=tk.W)
doctor_treeview.heading("Doctor Id", text="Doctor Id", anchor=tk.CENTER)
doctor_treeview.heading("Department", text="Department", anchor=tk.CENTER)
doctor_treeview.heading("Status", text="Status", anchor=tk.CENTER)
doctor_treeview.heading("Floor", text="Floor", anchor=tk.CENTER)

doctor_treeview.tag_configure('odd_row', background='white')
doctor_treeview.tag_configure('even_row', background='#E5E5E5')

# doctor items alignments
back_button_15.place(x=20, y=20)
doctor_treeview.pack(padx=3, pady=3)
doctor_treeview_frame.place(x=96, y=50)

window.mainloop()