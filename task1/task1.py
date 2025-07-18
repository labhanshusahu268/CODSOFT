import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tasks_count = int(input("Enter number of initial tasks:"))
task_list = []
due_dates = []
status_list = []

for i in range(tasks_count):
    task = input(f"Enter the task {i+1} :")
    dates = input(f"Enter the date for task {i+1}  (DD/MM/YYYY):")
    status = input(f"Enter the status of task {i+1} (completed/due) :").lower()

    task_list.append(task)
    due_dates.append(dates)
    status_list.append(status)

df = pd.DataFrame({
    "task": task_list,
    "dates":due_dates,
    "status":status_list,
})

def add_new__task():
    global df
    no_of_new_tasks = int(input(" How many new tasks you want to add ?:"))
    for i in range(no_of_new_tasks):
        task = input(f"Enter  new task {i+1} :")
        due_dates = input(f"Enter date for new task {i+1}  (DD/MM/YYYY):")
        status = input(f"Enter the status of new task {i+1}  (completed/due) :").lower()
        new_row = ({"task":task,"dates":dates,"status":status})
        df = pd.concat([df,pd.DataFrame([new_row])],ignore_index = True)
        print("New tasks added successfully ")


def show_task():
    print(df)
    print("Tasks print successfully ")

def searching_task():
    searching = input("search by (task/date)").lower()
    if searching == "date":
        search_date = input("enter the date for searching the task (e.g. 12/01/2025) :")
        searched_date = df[df["dates"] == search_date]
        print(f" Searched date is {searched_date} ")
        print("Searched Successfully ")

    elif searching == "task":
        search_task = input("enter the  task for searching :")
        searched_task = df[df["task"] == search_task]
        print(f"your searched task is {searched_task} :")
        print("Searched Successfully ")

    else:
        print("invalid search ")
        print("No Searching is possible ")


def delete_task():
    global df
    print(df)
    task_number = int(input("Enter the index of task that you want to delete :"))
    if 0<= task_number <len(df):
        x = df.drop(task_number)
        df.reset_index(drop=True)
        print("Task deleted successfuly ")
        print(f"After deleting remaining tasks are \n {x} :")
    else:
        print("Invalid index ")


def track_task():
    check_status = int(input("Enter the index of task for knowing its status :"))
    if 0 <= check_status < len(df): 
        print(df.iloc[[check_status]][['task', 'status']])
    else:
        print("invalid index given for checking status of task ")

def pie_chart():
    status_counts = df["status"].value_counts()
    labels = status_counts.index
    values = status_counts.values

    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=["red", "green"])
    plt.legend()
    plt.title(" Task Completion Status")
    plt.axis('equal') 
    plt.show()



print("\n OPTIONS :")
print("\n add / show / search / delete / status / chart / exit")

while(True):
    choice =  input("Enter your choice :").lower()
    if choice == "show":
         show_task()
    elif choice == "add":
         add_new__task()
    elif choice == "chart":
        pie_chart()
    elif choice == "search":
        searching_task()
    elif choice == "delete":
        delete_task()
    elif choice == "status":
        track_task()
    elif choice == "exit":
        print("ohk exiting .... BYE ")
        break
    else:
        print("Invalid choice ")









