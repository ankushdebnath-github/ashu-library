print("****WELCOME TO LIBRARY MANAGEMENT SYSTEM***")
import os
import sys

#To connect to the MySQL server
import mysql.connector
mydb=mysql.connector.connect(host='localhost',
                            user='root',passwd='ankush@121',
                             database='library');

def createTable():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='ankush@121', database='library')
    mycursor = mydb.cursor();
    query = '''CREATE TABLE books (
        student_id INT(20), 
        student_name VARCHAR(25), 
        date_of_issue DATE, 
        date_of_return DATE, 
        book_id INT(20) , 
        title VARCHAR(255) , 
        author VARCHAR(255) , 
        ISBN VARCHAR(255) , 
        stock INT(4) );'''
    myCursor.execute(query);
    mydb.commit()
    print('Table created successfully!')

def insRecord():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='ankush@121', database='library')
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES LIKE 'library'")
    result = mycursor.fetchone()
    if result:
        print('Table already exist')
    else:
        create_table()
    n = int(input("Enter how many books you want to add:"))
    for i in range(n):
       stid = int(input("enter student id:"))
       stname = input("Enter Student name: ")
       dateissue = input("Enter a date in the format of dd/mm/yyyy: ")
       datereturn = input("Enter a date in the format of dd/mm/yyyy for returning the book:")
       bookid =int(input("book id:"))
       tit = input('Enter the book title:')
       athr = input('Enter the author name:')
       IN = input('Enter the ISBN:')
       stck = int(input('Enter the stock:'))
       mycursor.execute("INSERT INTO books VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s)",(stid, stname,  dateissue, datereturn, bookid, tit, athr, IN, stck));
       mydb.commit()
       print("Record inserted successfully...")
def showRecord():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='ankush@121', database='library')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM books')
    mytable = mycursor.fetchall()
    print(mytable)
    rec_count = mycursor.rowcount
    print('Number of records in the given table:', rec_count)

def updateRecord():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='ankush@121',database='library')
    mycursor = mydb.cursor()
    book_id=int(input('Enter the book id to update:'))
    stock=int(input('Enter the new stock:'))
    mycursor.execute("UPDATE books SET stock=%s WHERE book_id=%s", (stock, book_id))
    mydb.commit()
    print("Record updated successfully...")

def deleteRecord():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='ankush@121',database='library')
    mycursor = mydb.cursor()
    book_id=int(input('Enter the book id to delete:'))
    mycursor.execute("DELETE FROM books WHERE book_id=%s", (book_id,))
    mydb.commit()
    print("Record deleted successfully...")

def findRecord():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='aknush@121',database='library')
    mycursor = mydb.cursor()
    book_id=input('Enter the book id to find:')
    mycursor.execute("SELECT * FROM books WHERE book_id=%s", (book_id,))
    result = mycursor.fetchone()
    if result:
        print("Record found: ", result)
    else:
        print("No record found with the given book ID.")

    
def sortRecord():
    field=input('Enter the field name to be sorted:')
    order=input('Enter the sort order (asc/desc):')
    myCursor=mydb.cursor()
    sqlStat="select * from coviddata order by "+field+" "+order
    myCursor.execute(sqlStat)
    myRec=myCursor.fetchall();
    for rec in myRec:
        print(rec)
    showRecord()

       
while True:

            print ("MENU \n 1-Library management \n 2-display \n 3-search \n 4-sort \n 5-delete \n 6-exit")
            ch=int(input ("enter your choice"))
            
    
            if ch==1:
                #createTable()
                insRecord()
                   
            elif ch==2:
                showRecord()
                   
            elif ch==3:
                findRecord()
            elif ch==4:
                sortRecord()
            elif ch==5:
                delRecord()
            elif ch==6:
                print("THANK YOU FOR USING")
                sys.exit()
            else:
                print("Invalid option. Retry")
                

    
    
    

