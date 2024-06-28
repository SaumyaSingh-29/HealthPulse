import mysql.connector
global mydb,mycursor
mydb = mysql.connector.connect(host="localhost",user="root",passwd="your_pwd",database="patients_database")
mycursor = mydb.cursor()


def add_patient():
    patient_ID = int(input("Enter patient ID : "))
    Patient_ID=str(patient_ID)
    Department=input("Enter patient department  : ")
    DoctorName=str(input("Enter name of doctor following the case : "))
    Name=str(input("Enter patient name   : "))
    Age=int(input("Enter patient age   : "))
    age=str(Age)
    Gender=str(input("Enter patient gender   : "))
    Address=str(input("Enter patient address  : "))
    RoomNumber=int(input("Enter patient room number   : "))
    Room_Number=str(RoomNumber)
   
    sql = "INSERT INTO patient(patient_id,department,doctor_name,patient_name,age,gender,address,room_no) VALUES ("+str(patient_ID)+",'"+Department+"','"+DoctorName+"','"+Name+"',"+str(Age)+",'"+Gender+"','"+Address+"',"+str(RoomNumber)+")"
    mycursor.execute(sql)
    mydb.commit()
    print("----------------------Patient added successfully----------------------")


def edit_patient():
    patient_ID=int(input("Enter patient ID : "))
    print("------------------------------------------")
    print("|To Edit patient Department Enter 1 :|")
    print("|To Edit Doctor following case Enter 2 :|")
    print("|To Edit patient Name Enter 3 :|")
    print("|To Edit patient Age Enter 4 :|")
    print("|To Edit patient Gender Enter 5 :|")
    print("|To Edit patient Address Enter 6 :|")
    print("|To Edit patient RoomNumber Enter 7 :|")
    print("-----------------------------------------")
    echoice=int(input("enter your choice :"))
    if echoice==1:
        dept=str(input("Enter new department :"))
        sql="update patient set department='"+dept+"' where patient_id="+str(patient_ID)+" "
        mycursor.execute(sql)
        mydb.commit()
        print("----------------------Patient Department edited successfully----------------------")
    elif echoice==2:
        doc=str(input("Enter new doctor name :"))
        sql="update patient set doctor_name='"+doc+"' where patient_id="+str(patient_ID)+" "
        mycursor.execute(sql)
        mydb.commit()
        print("----------------------Doctor following case edited successfully----------------------")
    elif echoice==3:
        pat=str(input("Enter new patient name :"))
        sql="update patient set patient_name='"+pat+"' where patient_id="+str(patient_ID)+" "
        mycursor.execute(sql)
        mydb.commit()
        print("----------------------Patient name edited successfully----------------------")
    elif echoice==4:
        ag=int(input("Enter patients age :"))
        sql="update patient set age="+str(ag)+" where patient_id="+str(patient_ID)+" "
        mycursor.execute(sql)
        mydb.commit()
        print("----------------------Patient age edited successfully----------------------")
    elif echoice==5:
        gen=str(input("Enter patient's gender :"))
        sql="update patient set gender='"+gen+"' where patient_id="+str(patient_ID)+" "
        mycursor.execute(sql)
        mydb.commit()
        print("----------------------Patient gender edited successfully----------------------")
    elif echoice==6:
        add=str(input("Enter new address :"))
        sql="update patient set address='"+add+"' where patient_id="+str(patient_ID)+" "
        mycursor.execute(sql)
        mydb.commit()
        print("----------------------Patient address edited successfully----------------------")
    elif echoice==7:
        room=int(input("Enter new room number :"))
        sql="update patient set room_no="+str(room)+" where patient_id="+str(patient_ID)+" "
        mycursor.execute(sql)
        mydb.commit()
        print("----------------------Patient RoomNumber edited successfully----------------------")
    else:
        print("Please Enter a correct choice :")
        
def del_patient():
    patient_ID = int(input("Enter patient ID : "))
    sql="delete from patient where patient_id="+str(patient_ID)+" "
    mycursor.execute(sql)
    mydb.commit()
    print("----------------------Patient data deleted successfully----------------------")


def disp_patient():
    patient_ID = int(input("Enter patient ID : "))
    mycursor.execute("select * from patient where patient_id="+str(patient_ID)+" ")
    myresult=mycursor.fetchall()
    for x in myresult:
        print(myresult)
    print("\npatient name        : ",x[3])
    print("patient age         : ",x[4])
    print("patient gender      : ",x[5])
    print("patient address     : ",x[6])
    print("patient room number : ",x[7])
    print("patient is in ",x[1],"Department")
    print("patient is followed by doctor : ",x[2])


def add_doc():
    Doctor_ID = int(input("Enter doctor ID : "))
    Department=input("Enter Doctor department : ")
    Name      =input("Enter Doctor name       : ")
    Address   =input("Enter Doctor address    : ")
    
    sql="insert into doctor(doctor_id,department,doctor_name,address) values("+str(Doctor_ID)+",'"+Department+"','"+Name+"','"+Address+"')"
    mycursor.execute(sql)
    mydb.commit()


    print("----------------------Doctor added successfully----------------------")

def edit_doc():
    Doctor_ID=input("Enter doctor ID : ")
    
    print("-----------------------------------------")
    print("|To Edit doctor's department Enter 1    |")
    print("|To Edit doctor's name Enter 2          |")
    print("|To Edit doctor's address Enter 3       |")
    print("-----------------------------------------")
    dchoice=input("Enter your choice : ")
    if dchoice == "1":
        dept=input("Enter Doctor's Department : ")
        sql="update doctor set department='"+dept+"' where doctor_id="+str(Doctor_ID)+" "
        mycursor.execute(sql)
        mydb.commit()
        
        print("/----------------------Doctor's department edited successfully----------------------/")
    elif dchoice == "2":
        name=input("Enter Doctor's Name : ")
        sql="update doctor set doctor_name='"+name+"' where doctor_id="+str(Doctor_ID)+" "
        mycursor.execute(sql)
        mydb.commit()
        print("----------------------Doctor's name edited successfully----------------------")
    elif dchoice == "3":
        add=input("Enter Doctor's Address : ")
        sql="update doctor set address='"+add+"' where doctor_id="+str(Doctor_ID)+" "
        mycursor.execute(sql)
        mydb.commit()
        print("----------------------Doctor's address edited successfully----------------------")
										
    
def disp_doc():
    Doctor_ID = int(input("Enter doctor ID : "))
    mycursor.execute("select * from doctor where doctor_id="+str(Doctor_ID)+" ")
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x)
    print("Doctor name    : ", x[2])
    print("Doctor address : ",x[3])
    print("Doctor Department :",x[1])
   



def book_appointment():
    

    print("---------------------------------------------------------")
    print("|For book an appointment for an exist patient Enter 1")
    print(" For book an appointment for a new patient enter 2")
    print("---------------------------------------------------------")


    achoice=int(input("enter your choice :"))
    
    if achoice==1:
        patient_ID = int(input("Enter patient ID : "))
        sql="select appointment_start, appointment_end from patient where appointment_start is NOT NULL"
        mycursor.execute(sql)
        myresult=mycursor.fetchall()
        for x in myresult:
            print(x)
        print("These are the already booked appointments, please choose timings accordingly")
        session_start=str(input("Enter the start timings :"))
        session_end=str(input("Enter the end timing :"))
        abc="update patient set appointment_start='"+session_start+"' where patient_id="+str(patient_ID)+" "
        mycursor.execute(abc)
        mydb.commit()
        xyz="update patient set appointment_end='"+session_end+"' where patient_id="+str(patient_ID)+" "
        mycursor.execute(xyz)
        mydb.commit()
        print("-----------------------Appointment booked successfully----------------------")

    elif achoice==2:
        patient_ID = int(input("Enter patient ID : "))
        Department=input("Enter department :")
        DoctorName=input("Enter Doctor name :")
        Name=input("Enter patient name    : ")
        Age=int(input("Enter patient age     : "))
        Gender=input("Enter patient gender  : ")
        Address=input("Enter patient address : ")
        RoomNumber=int(input("Enter Room number :"))

        sql = "INSERT INTO patient(patient_id,department,doctor_name,patient_name,age,gender,address,room_no) VALUES ("+str(patient_ID)+",'"+Department+"','"+DoctorName+"','"+Name+"',"+str(Age)+",'"+Gender+"','"+Address+"',"+str(RoomNumber)+")"
        mycursor.execute(sql)
        mydb.commit()
        sql="select appointment_start,appointment_end from patient where appointment_start is NOT NULL"
        mycursor.execute(sql)
        myresult=mycursor.fetchall()
        for x in myresult:
            print(x)
        print("These are the already booked appointments, please choose timings accordingly")
        session_start=input("Enter the start timings :")
        session_end=input("Enter the end timing :")
        abc="update patient set appointment_start='"+session_start+"' where patient_id="+str(patient_ID)+" "
        mycursor.execute(abc)
        mydb.commit()
        xyz="update patient set appointment_end='"+session_end+"' where patient_id="+str(patient_ID)+" "
        mycursor.execute(xyz)
        mydb.commit()
        print("/----------------------Appointment booked successfully----------------------/")
										

def edit_appointment():
    patient_ID = int(input("Enter patient ID : "))
    sql="select appointment_start,appointment_end from patient where appointment_start is NOT NULL"
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x)
    print("These are the already booked appointments, please choose timings accordingly")
    Session_Start_new = input ("Please enter the new start time : ")
    Session_End = input ("Please enter the new end time : ")
    sql="update patient set appointment_start='"+Session_Start_new+"' where patient_id= "+str(patient_ID)+" "
    mycursor.execute(sql)
    mydb.commit()
    mysql="update patient set appointment_end='"+Session_End+"' where patient_id= "+str(patient_ID)+" "
    mycursor.execute(mysql)
    mydb.commit()
    print("/----------------------appointment edited successfully----------------------/")



def cancel_appointment():
    patient_ID = int(input("Enter patient ID : "))
    sql="update patient set appointment_start= NULL where patient_id= "+str(patient_ID)+" "
    mycursor.execute(sql)
    mydb.commit()
    mysql="update patient set appointment_end= NULL where patient_id= "+str(patient_ID)+" "
    mycursor.execute(mysql)
    mydb.commit()
    print("/----------------------appointment canceled successfully----------------------/")





#defining variables
Patients_Dict = dict()
Patient_ID = ""
Department = ""
Doctor_Name = ""
Patient_Name = ""
Patient_Age = ""
Patient_Gender = ""
Patient_Address = ""
RoomNumber = ""


#MENU
print("********************MENU*******************************")
print("1. Enter patient's details")
print("2. Edit patient's details")
print("3. Delete patient's details")
print("4. Display patient's details")
print("5. Enter doctor's details")
print("6. Edit doctor's details")
print("7. Display doctor's details")
print("8. Book an appointment")
print("9. Edit an appointment")
print("10. Cancel an appointment")



#Input the choice
choice= int(input("enter your choice :"))


if choice==1 :
    add_patient()
    
elif choice==2:
    edit_patient()
    
elif choice==3:
    del_patient()
    
elif choice==4:
    disp_patient()
    
elif choice==5:
    add_doc()
    
elif choice==6:
    edit_doc()
    
elif choice==7:
    disp_doc()
    
elif choice==8:
    book_appointment()
    
elif choice==9:
    edit_appointment()
    
elif choice==10:
    cancel_appointment()
else:
    print("Enter choice between 1 to 10")
    
