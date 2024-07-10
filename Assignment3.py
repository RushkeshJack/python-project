from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.school
students = db.students

def insert_data():
    students.insert_many([
        {'SID': 1, 'SNAME': 'John Doe', 'COURSE': 'Math', 'MARKS': 85},
        {'SID': 2, 'SNAME': 'Jane Smith', 'COURSE': 'Science', 'MARKS': 90},
        {'SID': 3, 'SNAME': 'Emily Davis', 'COURSE': 'History', 'MARKS': 75},
        {'SID': 4, 'SNAME': 'Michael Brown', 'COURSE': 'Art', 'MARKS': 88}
    ])
    print("Data inserted successfully")

def update_marks():
    students.update_one({'SID': 3}, {'$set': {'MARKS': 92}})
    print("Marks updated successfully")


def display_records():
    for student in students.find():
        print(student)


def delete_student():
    students.delete_one({'SID': 4})
    print("Student 4 deleted successfully")


insert_data()
update_marks()
display_records()
delete_student()
