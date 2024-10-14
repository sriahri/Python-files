import sqlite3

        #TO CREATE A DATABASE

def create_Database():
    try:
        sqliteConnection = sqlite3.connect('school.db')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")

        sqlite_select_Query = "select sqlite_version();"
        cursor.execute(sqlite_select_Query)
        record = cursor.fetchall()
        print("SQLite Database Version is: ", record)
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

            # TO CREATE A STUDENTS TABLE

def create_table_students():
    try:
        sqliteConnection = sqlite3.connect('school.db')
        sqlite_create_table_query = '''CREATE TABLE students (id varchar(15)
                                        primary key,name varchar(30),maths
                                        real default 0,physics real default
                                         0,chemistry real default 0,biology 
                                         real default 0,english real default
                                          0,hindi real default 0);'''

        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        print("Students table created")

        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

            #CREATE A TEACHERS TABLE

def create_table_teachers():
    try:
        sqliteConnection = sqlite3.connect('school.db')
        sqlite_create_table_query = '''CREATE TABLE teachers(id varchar(15)
                                        primary key,name varchar(30) not null,
                                        subject varchar(20) not null,salary 
                                        real default 5000);'''

        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        print("Teachers table created")

        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

        #TO ADD STUDENT'S DATA TO THE TABLE

def data_entry_students(id, name,maths,physics,chemistry,biology,english,hindi):
    try:
        sqliteConnection = sqlite3.connect('school.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_query = """INSERT INTO students
                              (id, name,maths,physics,chemistry,biology,english,hindi) 
                               VALUES 
                              (?,?,?,?,?,?,?,?);"""
        data_tuple=(id, name,maths,physics,chemistry,biology,english,hindi)
        count = cursor.execute(sqlite_insert_query,data_tuple)
        sqliteConnection.commit()
        print("Record inserted successfully into students table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into students table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

            #TO ADD DATA INTO TEACHERS TABLE

def data_entry_teachers(id, name,subject,salary):
        try:
            sqliteConnection = sqlite3.connect('school.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            sqlite_insert_query = """INSERT INTO teachers
                                  (id, name,subject,salary) 
                                   VALUES 
                                  (?,?,?,?);"""
            data_tuple=(id, name,subject,salary)
            count = cursor.execute(sqlite_insert_query,data_tuple)
            sqliteConnection.commit()
            print("Record inserted successfully into teachers table ", cursor.rowcount)
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert data into teachers table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")

            #TO DELETE STUDENT'S RECORD FROM THE TABLE

def delete_data_students(id):
    try:
        sqliteConnection = sqlite3.connect('school.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sql_update_query = """DELETE from students where id = ?"""
        cursor.execute(sql_update_query, (id,))
        sqliteConnection.commit()
        print("Record deleted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a student table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

            #TO DELETE A RECORD FROM TEACHERS TABLE

def delete_data_teachers(id):
    try:
        sqliteConnection = sqlite3.connect('school.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sql_update_query = """DELETE from teachers where id = ?"""
        cursor.execute(sql_update_query, (id,))
        sqliteConnection.commit()
        print("Record deleted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a teachers table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

        #TO RETRIEVE DATA OF A PARTICULAR STUDENT PRESENT IN THE TABLE

def getStudentInfo(id):
    try:
        sqliteConnection = sqlite3.connect('school.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from students where id = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        print("Printing ID ", id)
        for row in records:
            print("Name = ", row[1])
            print("Marks scored in Maths  = ", row[2])
            print("Marks scored in Physics  = ", row[3])
            print("Marks scored in Chemistry  = ", row[4])
            print("Marks scored in Biology  = ", row[5])
            print("Marks scored in English  = ", row[6])
            print("Marks scored in Hindi  = ", row[7])
            total=(row[2]+row[3]+row[4]+row[5]+row[6]+row[7])
            average=total/6
            print("The total marks of student bearing ", id + " is ", total)
            print("The average marks of student bearing ",id + " is ",average)
            if average >91:
                grade='A'
            elif average>81:
                grade='B'
            elif average>71:
                grade='C'
            elif average>61:
                grade='D'
            elif average>51:
                grade='E'
            else:
                grade='F'
            print('The grade of the student is : ',grade)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from students table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

            #TO RETRIEVE THE DATA OF THE TEACHER

def getTeacherInfo(id):
    try:
        sqliteConnection = sqlite3.connect('school.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sql_select_query = """select * from teachers where id = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        print("Printing ID ", id)
        for row in records:
            print("Name = ", row[1])
            print("Subject taught by the teacher is : ", row[2])
            print("Salary of the teacher is  = ", row[3])
            cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from teachers table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

            #CREATING A SIMPLE FUNCTION THAT PRINTS THE NAME OF A PARTICULAR STUDENT IN TITLE

def _toTitleCase(string):
    return str(string).title()

def getStudentName(id):
    try:
        sqliteConnection = sqlite3.connect('school.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqliteConnection.create_function("TOTITLECASE", 1, _toTitleCase)
        select_query = "SELECT TOTITLECASE(name) FROM students where id = ?"
        cursor.execute(select_query, (id,))
        name = cursor.fetchone()
        print("Student Name is : ", name)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from student table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

while 1:
    print('1 : TO CREATE DATABASE')
    print('2 : TO CREATE STUDENTS TABLE')
    print('3 : TO CREATE TECHERS TABLE')
    print('4 : TO INSERT DATA INTO STUDENTS TABLE')
    print('5 : TO INSERT DATA INTO TEACHERS TABLE')
    print('6 : TO DELETE A RECORD FROM STUDENTS TABLE')
    print('7 : TO DELETE A RECORD FROM TEACHERS TABLE')
    print('8 : TO RETRIEVE INFROMATION OF A PARTICULAR STUDENT')
    print('9 : TO RETRIEVE INFROMATION OF A PARTICULAR TEACHER')
    print('10 : TO GIVE THE NAME OF A STUDENT IN TITLECASE')
    print('IF YOU WANT TO EXIT PRESS -1')
    print('PLEASE SELECT THE OPTIONS ABOVE TO PERFORM THE REQUIRED OPERATION :  ',end='')
    n=int(input())
    if n==1:
        print()
        create_Database()
        print()
    elif n==2:
        print()
        create_table_students()
        print()
    elif n==3:
        print()
        create_table_teachers()
        print()
    elif n==4:
        print()
        id = input('enter the id of the student : ')
        name = input('enter the name of the student : ')
        maths = int(input('enter the marks of the student scored in mathematics : '))
        physics = int(input('enter the marks of the student scored in physics : '))
        chemistry = int(input('enter the marks of the student scored in chemistry : '))
        biology = int(input('enter the marks of the student scored in biology : '))
        english = int(input('enter the marks of the student scored in english : '))
        hindi = int(input('enter the marks of the student scored in hindi : '))
        data_entry_students(id, name,maths,physics,chemistry,biology,english,hindi)
        print()
    elif n==5:
        print()
        id = input('Enter the id of the teacher : ')
        name = input('Enter the name of the teacher : ')
        subject = input('Enter the name of the subject : ')
        salary = float(input('Enter the salary of the teacher : '))
        print()
        data_entry_teachers(id, name,subject,salary)
        print()
    elif n==6:
        print()
        id = input('Enter the id of a student you would like to delete : ')
        print()
        delete_data_students(id)
        print()
    elif n==7:
        print()
        id = input('Enter the id of a teacher you would like to delete : ')
        print()
        delete_data_teachers(id)
        print()
    elif n==8:
        print()
        id = input('Enter the id of the student to retrieve data : ')
        print()
        getStudentInfo(id)
        print()
    elif n==9:
        print()
        id = input('Enter the id of the teacher to retrieve data : ')
        print()
        getTeacherInfo(id)
        print()
    elif n==10:
        print()
        id = input('Enter the id of the student whose name is required : ')
        print()
        getStudentName(id)
        print()
    else:
        exit(1)
