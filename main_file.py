from tkinter import *
from tkinter import ttk
import postgresql_commands


def select_item(event):
    global item_id
    global selected_item
    index = database.selection()
    selected_item = database.item(index)
    item_id = selected_item['values'][0]

    person_id_entry.configure(state="normal")
    person_id_entry.delete(0, END)
    person_id_entry.insert(END, selected_item['values'][0])
    person_id_entry.configure(state="readonly")
    first_name_entry.delete(0, END)
    first_name_entry.insert(END, selected_item['values'][1])
    last_name_entry.delete(0, END)
    last_name_entry.insert(END, selected_item['values'][2])
    gender_entry.delete(0, END)
    gender_entry.insert(END, selected_item['values'][3])
    birth_date_entry.delete(0, END)
    birth_date_entry.insert(END, selected_item['values'][4])
    job_entry.delete(0, END)
    job_entry.insert(END, selected_item['values'][5])
    email_entry.delete(0, END)
    email_entry.insert(END, selected_item['values'][6])
    salary_entry.delete(0, END)
    salary_entry.insert(END, selected_item['values'][7])
    hired_date_entry.delete(0, END)
    hired_date_entry.insert(END, selected_item['values'][8])
    warning_strike_entry.delete(0, END)
    warning_strike_entry.insert(END, selected_item['values'][9])


def populate_list():
    index = 0
    database.delete(*database.get_children())
    for rows in postgresql_commands.fetch_data():
        database.insert("", index, values=rows)
        index = index + 1


def add_item():
    postgresql_commands.insert_data(first_name.get(), last_name.get(), gender.get(), birth_date.get(), job.get(),
                                    email.get(), salary.get(), hired_date.get(), warning_strike.get())
    database.insert("", END, (first_name.get(), last_name.get(), gender.get(), birth_date.get(), job.get(), email.get(),
                              salary.get(), hired_date.get(), warning_strike.get()))
    populate_list()


def delete_item():
    postgresql_commands.remove_data(item_id)
    clear_item()
    populate_list()


def update_item():
    postgresql_commands.update_data(first_name.get(), last_name.get(), gender.get(), birth_date.get(), job.get(),
                                    email.get(), salary.get(), hired_date.get(), warning_strike.get(), item_id)
    clear_item()
    populate_list()


def clear_item():
    person_id_entry.configure(state="normal")
    person_id_entry.delete(0, END)
    person_id_entry.configure(state="readonly")
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    gender_entry.delete(0, END)
    birth_date_entry.delete(0, END)
    job_entry.delete(0, END)
    email_entry.delete(0, END)
    salary_entry.delete(0, END)
    hired_date_entry.delete(0, END)
    warning_strike_entry.delete(0, END)


# Create window
app = Tk()
app.title("Emplpoyees Database")
app.geometry("1020x650")
app.resizable(width=FALSE, height=FALSE)

# Employee info input

person_id = StringVar()
person_id_label = Label(app, text='Person ID:', pady=20)
person_id_label.grid(row=0, column=0, sticky=W)
person_id_entry = Entry(app, textvariable=person_id, state='readonly')
person_id_entry.grid(row=0, column=1)

first_name = StringVar()
first_name_label = Label(app, text='First Name:', pady=20)
first_name_label.grid(row=0, column=2, sticky=W)
first_name_entry = Entry(app, textvariable=first_name)
first_name_entry.grid(row=0, column=3)

last_name = StringVar()
last_name_label = Label(app, text='Last Name:', pady=20)
last_name_label.grid(row=0, column=4, sticky=W)
last_name_entry = Entry(app, textvariable=last_name)
last_name_entry.grid(row=0, column=5, sticky=W)

gender = StringVar()
gender_label = Label(app, text='Gender:', pady=20)
gender_label.grid(row=0, column=6, sticky=W)
gender_entry = Entry(app, textvariable=gender)
gender_entry.grid(row=0, column=7)

birth_date = StringVar()
birth_date_label = Label(app, text='Birth date:', pady=20)
birth_date_label.grid(row=0, column=8, sticky=W)
birth_date_entry = Entry(app, textvariable=birth_date)
birth_date_entry.grid(row=0, column=9)

job = StringVar()
job_label = Label(app, text='Job:', pady=20)
job_label.grid(row=1, column=0, sticky=W)
job_entry = Entry(app, textvariable=job)
job_entry.grid(row=1, column=1)

email = StringVar()
email_label = Label(app, text='E-mail:', pady=20)
email_label.grid(row=1, column=2, sticky=W)
email_entry = Entry(app, textvariable=email)
email_entry.grid(row=1, column=3)

salary = StringVar()
salary_label = Label(app, text='Gross Salary:', pady=20)
salary_label.grid(row=1, column=4, sticky=W)
salary_entry = Entry(app, textvariable=salary)
salary_entry.grid(row=1, column=5)

hired_date = StringVar()
hired_date_label = Label(app, text='Hired Date:', pady=20)
hired_date_label.grid(row=1, column=6, sticky=W)
hired_date_entry = Entry(app, textvariable=hired_date)
hired_date_entry.grid(row=1, column=7)

warning_strike = StringVar()
warning_strike_label = Label(app, text='Warning Strike:', pady=20)
warning_strike_label.grid(row=1, column=8, sticky=W)
warning_strike_entry = Entry(app, textvariable=warning_strike)
warning_strike_entry.grid(row=1, column=9)

# Box tree for data visualization

database = ttk.Treeview(app, height=21)
database.grid(row=3, column=0, columnspan=11, rowspan=5, padx=15)
database["columns"] = ("id", "First Name", "Last Name", "Gender", "Birth Date", "Job", "E-mail", "Gross Salary",
                       "Hired Date", "Warning Strikes")
database["show"] = "headings"
database.heading("#0", text="ID", anchor="w")
database.column("#0", width=100)
database.heading("id", text="ID", anchor="w")
database.column("id", width=33)
database.heading("First Name", text="First Name", anchor="w")
database.column("First Name", width=78)
database.heading("Last Name", text="Last Name", anchor="w")
database.column("Last Name", width=78)
database.heading("Gender", text="Gender", anchor="w")
database.column("Gender", width=50)
database.heading("Birth Date", text="Birth Date", anchor="w")
database.column("Birth Date", width=67)
database.heading("Job", text="Job", anchor="w")
database.column("Job", width=220)
database.heading("E-mail", text="E-mail", anchor="w")
database.column("E-mail", width=220)
database.heading("Gross Salary", text="Gross Salary", anchor="w")
database.column("Gross Salary", width=75)
database.heading("Hired Date", text="Hired Date", anchor="w")
database.column("Hired Date", width=67)
database.heading("Warning Strikes", text="Warning Strikes", anchor="w")
database.column("Warning Strikes", width=85)

# Scrollbar for the database tree view

database_scrollbar = ttk.Scrollbar(app)
database_scrollbar.grid(row=3, column=10, sticky="ns", rowspan=5)

# Set scrollbar to tree view

database_scrollbar.configure(command=database.yview)
database.config(yscrollcommand=database_scrollbar.set)

# Bind select

database.bind("<<TreeviewSelect>>", select_item)


# Buttons

insert_data = Button(app, text='Insert Data', width=12, command=add_item)
insert_data.grid(row=2, column=0, pady=20, columnspan=12, sticky=W, padx=100)

delete_data = Button(app, text='Delete Data', width=12, command=delete_item)
delete_data.grid(row=2, column=1, columnspan=12, sticky=W, padx=180)

update_data = Button(app, text='Update Data', width=12, command=update_item)
update_data.grid(row=2, column=2, columnspan=12, sticky=W, padx=260)

clear_data = Button(app, text='Clear Entries', width=12, command=clear_item)
clear_data.grid(row=2, column=3, columnspan=12, sticky=W, padx=340)

# Get data from database to insert on the tree view box
populate_list()

# Start the app

mainloop()
