from datetime import datetime
import mysql.connector
mydb =mysql.connector.connect(host='localhost',user='root',password='jan2008lucknow',database='libraryn') 
mycursor=mydb.cursor()

def addmember():
        member=input('Enter a member add_member - ')
        name=input('Enter member - ')
        phoneno=int(input('Enter phone_number - '))
        email=input('Enter email - ')
        address=input('Enter address - ')
        current_datetime=datetime.now()

        query = "INSERT INTO MEMBERS (join_date, name, email, address) VALUES (%s, %s, %s, %s)"
        values = (current_datetime, name, email, address)

        user = mycursor.execute(query, values)
        mydb.commit()

        # Retrive saved user data
        query = "SELECT * FROM MEMBERS WHERE email = %s"
        mycursor.execute(query, (email,))
        saved_user = mycursor.fetchone()
        print('User data saved successfully. User Id: ', saved_user[0])
                                       
def addbook():
        addbook=input('Enter book_name - ')
        book_id=int(input('Enter book_id - '))
        title=input('Enter title - ')
        author=input('Author name - ')
        genre=input('Enter genre of book - ')
        isbn=int(input('Enter ISBN - '))
        publication_year=int(input('Enter publication_year - '))
        status=input('Enter status of book - ')
        query1="INSERT INTO BOOKS(bookid,title,author,genre,isbn,publication_year,status) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        values1=(book_id,title,author,genre,isbn,publication_year,status)
        mycursor.execute(query1,values1)
        mydb.commit()
        print('done!')

def borrowbook():
        borrowbook=input('Enter borrow_book - ')
        borrowing_id=int(input('Enter borrowing_id - '))
        book_id=int(input('Enter book_id - '))
        member_id=int(input('Enter member_id - '))
        fine=int(input('Enter fine - '))
        join_date_str=input('Enter join date (YYYY-MM-DD) - ')
        join_date = datetime.strptime(join_date_str, '%Y-%m-%d')
        query2="INSERT INTO BORROWING(borrowing_id,book_id,member_id,fine,borrow_date) VALUES(%s, %s, %s, %s,%s)"
        value2=(borrowing_id,book_id,member_id,fine,join_date)
        mycursor.execute(query2,value2)
        mydb.commit()
        print('done!!')

def returnbook():
        returnbook=input('Enter return_book')
        borrowing_id=int(input('Enter borrowing_id - '))
        book_id=int(input('Enter book_id - '))
        member_id=int(input('Enter member_id - '))
        returning_id=int(input('Enter returning_id - '))
        fine=int(input('Enter fine - '))
        join_date_str1=input('Enter join date (YYYY-MM-DD) - ')
        join_date1= datetime.strptime(join_date_str1, '%Y-%m-%d')

        query3="UPDATE BORROWING SET RETURN_DATE=%s WHERE BORROWING_ID=%s"
        values3=(join_date1,borrowing_id)
        mycursor.execute(query3,values3)
        mydb.commit()
        print("done!!!")

def seemembers():
     mycusor=mydb.cursor()
     query="select * from members"
     mycursor.execute(query)
     records=mycursor.fetchall()
     for row in records:
          print(row)
     print('done')
     
def seebooks():
     mucursor=mydb.cursor()
     query="select * from books"
     mycursor.execute(query)
     records=mycursor.fetchall()
     for row in records:
          print(row)
     print("done")

def borrowing():
     mucursor=mydb.cursor()
     query="select * from borrowing"
     mycursor.execute(query)
     records=mycursor.fetchall()
     for row in records:
          print(row)
     print("done")
     
     

# def fun():
#     choice=int(input('enter any choice- in fun'))
#     if choice==1:
#         addmember()
#     elif choice==2:
#         addbook()
#     elif choice==3:
#         borrowbook()
#     elif choice==4:
#         returnbook()
#     else:
#         print('invalid option - ')
# fun()

# def options():
#         a="choice 1 = add member"
#         b="choice 2= add book "
#         c="choice 3= borrow book"
#         d="choice 4= return book"
#         print(a)
#         print(b)
#         print(c)
#         print(d)
def options():
      a='''Choose an option
1. Add member
2. Add book 
3. Borrow book
4. Return book
5. See all members
6. See all books
7. See borrowing'''
      print(a)       
  
def fun():
    show = options()
    choice=int(input('Enter any choice - '))
    if choice==1:
        addmember()
    elif choice==2:
        addbook()
    elif choice==3:
        borrowbook()
    elif choice==4:
        returnbook()
    elif choice==5:
        a='see all members'
        print(a)
        seemembers()
    elif choice==6:
        b='see all books'
        print(b)
        seebooks()
    elif choice==7:
        c='see borrowings'
        print(c)
        borrowing()
    else:
        print('Invalid option - ')
fun()
