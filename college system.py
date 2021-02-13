# INITIAL ----------------------------------------------------------------------------------------------
# https://www.youtube.com/watch?v=zQuWu6pcqNw&ab_channel=johangodinho
import os
import mysql.connector as mysql



# CONNECT TO DATABASE MYSQL ----------------------------------------------------------------------------
db  = mysql.connect(host='localhost', user='root', password='', database='college')
# to execute query as delete, select, etc
commander_handler =  db.cursor(buffered=True)


# -------------------------------------------------------------------------------------------------------
# ----  STUDENT SESSION 
# -------------------------------------------------------------------------------------------------------
def student_session(username):
    while 1:
        print("")
        print("Sudent's Menu")
        print("")
        print("1. View Register")
        print("2. Download Register")
        print("3. Logout")

        user_option  = input(str("Option : "))
        if user_option == "1":
            print("Displaying register")
            username =  (str(username),)
            commander_handler.execute("SELECT date, username, status FROM attendance WHERE username = %s", username)
            records =  commander_handler.fetchall()
            for record in records:
                print(record)

        if user_option == "2":
            print("Downloading Register")
            username =  (str(username),)
            commander_handler.execute("SELECT date, username, status FROM attendance WHERE username = %s", username)
            records =  commander_handler.fetchall()
            for record in records:
                with open('C:/Users/lmanu/Desktop/college/register.txt', 'w') as f:
                    f.write(str(records) + "\n")
                f.close()
            print("All records saved")
        elif user_option == "3":
            break
        else:
            print("No valid option was selected")

# STUDENT --> functions
def auth_student():
    print("")
    print("Student Login")
    print("")
    username =  input(str("Username : "))
    password = input(str("Password : "))
    # Query database
    query_vals = (username, password)
    commander_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilege = 'student'", query_vals)
    if commander_handler.rowcount < 1:
        print("Login not rocognised")
    else:
        #print(f"Welcome student, {query_vals[0]}!")
        student_session(username)





# -------------------------------------------------------------------------------------------------------
# ----  TEACHER 
# -------------------------------------------------------------------------------------------------------
# TEACHER --> functions
def teacher_session():
    while 1:
        print("")
        print("Teacher's Menu")
        print("1. Mark student register")
        print("2. View register")
        print("3. Logout")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            print("Mark student register")
            commander_handler.execute("SELECT username FROM users WHERE privilege = 'student'")
            records = commander_handler.fetchall()
            date    = input(str('Date : DD/MM/YYYY : '))
            for record in records:
                record = str(record).replace("'", "")
                record = str(record).replace(",", "")
                record = str(record).replace("'", "")
                record = str(record).replace("(", "")
                record = str(record).replace(")", "")
                # Present | Absent | Late
                status = input(str("Status for " +  str(record) + " : P/A/L : "))
                query_vals = (str(record), date, status)
                commander_handler.execute("INSERT INTO attendance (username, date, status) VALUES(%s,%s,%s)", query_vals)
                db.commit()
                print(record + " Marked as " + status)
        elif user_option == "2":
            print("")
            print("Viewing all student students registered")
            commander_handler.execute("SELECT username, date, status FROM attendance ")
            records = commander_handler.fetchall()
            print("Displaying all registers")
            for record in records:
                print(record)
        elif user_option == "3":
            break
        else:
            print("No valid option was selected")



def auth_teacher():
    print("")
    print("Teacher Login")
    print("")
    username = input(str('Username : '))
    password = input(str('Password : '))
    # query database
    query_vals  = (username, password)
    commander_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilege = 'teacher'", query_vals)
    if commander_handler.rowcount < 1:
        print("Login not reconised")
    else:
        # ------ teacher_session --------------------
        teacher_session()
        print(f"Welcome teacher, {query_vals[0]}")





# -------------------------------------------------------------------------------------------------------
# ----  ADMIN SESSION 
# -------------------------------------------------------------------------------------------------------
def admin_session():
    while 1:
        print("")
        print("Admin Menu")
        print("1. Register new Student")
        print("2. Register new Teacher")
        print("3. Delete existing Student")
        print("4. Delete existing Teacher")
        print("5. Logout")
        
        # to register a studet on database (variables, username, password and 'privilege':[student, teacher, adim] )
        user_option = input(str('Option : '))
        if user_option == '1':
            print("")
            print("Register New Student")
            username = input(str("Student username : "))
            password = input(str("Student password : "))
            query_vals =  (username, password)
            commander_handler.execute("INSERT INTO users (username, password, privilege) VALUES (%s,%s, 'student')", query_vals)
            db.commit()
            print(username + ' has been registered as a student')
        
        # to register teacher on database
        elif user_option == '2':
            print("")
            print("Register New Teacher")
            username = input(str("Teacher username : "))
            password = input(str("Teacher password : "))
            query_vals =  (username, password)
            commander_handler.execute("INSERT INTO users (username, password, privilege) VALUES (%s,%s, 'teacher')", query_vals)
            db.commit()
            print(username + ' has been registered as a teacher')
        
        # to delete a student account on database
        elif user_option == '3':
            print("")
            print("Delete existing Student Account")
            username = input(str("Student username : "))
            query_vals =  (username, 'student')
            commander_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s", query_vals)
            db.commit()
            # find out if the were any username deleted
            if commander_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + " has been deleted")

        # to delete a teacher account on database
        elif user_option == '4':
            print("")
            print("Delete existing Teacher Account")
            username = input(str("Teacher username : "))
            query_vals =  (username, 'teacher')
            commander_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s", query_vals)
            db.commit()
            # find out if the were any username deleted
            if commander_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + " has been deleted")      
        
        # Logout
        elif user_option == '5':
            break
        else:
            print("No valid option selected")



# ADMIN   --> functions
def auth_admin():
    print("")
    print("Admin Login")
    print("")
    username =  input(str("Username : "))
    password = input(str("Password : "))
    if username == "admin":
        if password  == "password":
            # ------ admin_session --------------------
            admin_session()
        else:
            print("Incorrect password !")
    else:
        print("Login details not recognised")

    

# -------------------------------------------------------------------------------------------------------
# ----  MAIN
# -------------------------------------------------------------------------------------------------------

def main():
    attempt = 0
    while 1:
        #  Greeting
        print('Welcome to the college system\n')
        # Privilege types (admin, teahcer, student)
        print('1. Login as student')
        print('2. Login as teacher')
        print('3. Login as admin')

        user_option = input(str("Option : "))
        print("")

        # 1: STUDENT
        if user_option ==  "1":
            #print("Student login")
            auth_student()
        # 2: TEACHER
        elif user_option == "2":
            #print('Teacher login')
            auth_teacher()
        # 3: ADMIN
        elif user_option == "3":
            #print('Admin login')
            auth_admin()
        # ANSWER: UNAVAILABLE
        else:
            print("No valid option was selected")
        print('\n\n')
        if attempt >= 3:
            break
        attempt =+ 1


main()
