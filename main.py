from datetime import datetime
import mysql.connector
from tabulate import tabulate

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
        print("\n")
        print('\033[1m' + 'User data saved successfully. User Id: ' + str(saved_user[0]) + '\033[0m')
                                       
def addbook():
        addbook=input('Enter book_name - ')
        title=input('Enter title - ')
        author=input('Author name - ')
        genre=input('Enter genre of book - ')
        isbn=int(input('Enter ISBN - '))
        publication_year=int(input('Enter publication_year - '))
        status=input('Enter status of book - ')
        query1="INSERT INTO BOOKS(title,author,genre,isbn,publication_year,status) VALUES( %s, %s, %s, %s, %s, %s)"
        values1=(title,author,genre,isbn,publication_year,status)
        mycursor.execute(query1,values1)
        mydb.commit()
        
        # Retrive saved user data
        query = "SELECT * FROM BOOKS WHERE title = %s"
        mycursor.execute(query, (title,))
        saved_book = mycursor.fetchone()
        print("\n")
        print('\033[1m' + 'Data saved successfully. Book Id: ' + str(saved_book[0]) + '\033[0m')

def borrowbook():
        borrowbook=input('Enter borrow_book - ')
        book_id=int(input('Enter book_id - '))
        member_id=int(input('Enter member_id - '))
        borrow_date=input('Enter join date (YYYY-MM-DD) - ')
        due_date=input('Enter due date (YYYY-MM-DD) - ')
        borrow_date = datetime.strptime(borrow_date, '%Y-%m-%d')
        due_date=datetime.strptime(due_date, '%Y-%m-%d')
        query2="INSERT INTO BORROWING(book_id,member_id,fine,borrow_date,due_date) VALUES(%s, %s,0,%s,%s)"
        value2=(book_id,member_id,borrow_date,due_date)
        mycursor.execute(query2,value2)
        mydb.commit()

        # Retrive saved user data
        query = "SELECT * FROM BORROWING WHERE member_id = %s"
        mycursor.execute(query, (member_id,))
        saved_borrowing = mycursor.fetchone()
        print("\n")
        print('\033[1m' + 'Data saved successfully. Borrowing Id: ' + str(saved_borrowing[0]) + '\033[0m')


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
    mycursor = mydb.cursor()
    query = "select * from members"
    mycursor.execute(query)
    records = mycursor.fetchall()
    headers = ["Member Id", "Joining Date", "Name", "Email", "Address"]
    print(tabulate(records, headers, tablefmt="pretty"))
     
def seebooks():
    mycursor = mydb.cursor()
    query = "select * from books"
    mycursor.execute(query)
    records = mycursor.fetchall()
    
    # Define column headers
    headers = ["Book ID", "Title", "Author", "Genre", "ISBN", "Publication Year", "Status"]
    
    # Print the table
    print(tabulate(records, headers, tablefmt="pretty"))

def borrowing():
    mycursor = mydb.cursor()
    query = "select * from borrowing"
    mycursor.execute(query)
    records = mycursor.fetchall()
    headers = ["Borrowing ID", "Book ID", "Member ID", "Borrow Date", "Due Date", "Return Date", "Fine"]
    print(tabulate(records, headers, tablefmt="pretty"))
     
     

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
    print("\n" + "-"*50)
    print("Library Management Application".center(50))
    print("-"*50 + "\n")
    print("Choose an option:")
    print("1. Add member")
    print("2. Add book")
    print("3. Borrow book")
    print("4. Return book")
    print("5. See all members")
    print("6. See all books")
    print("7. See borrowings")
    print("\n" + "-"*50)      
  
def fun():
    options()
    choice = int(input('Enter your choice: '))
    print("\n" + "-"*50)
    if choice == 1:
        addmember()
    elif choice == 2:
        addbook()
    elif choice == 3:
        borrowbook()
    elif choice == 4:
        returnbook()
    elif choice == 5:
        seemembers()
    elif choice == 6:
        print("See all books")
        seebooks()
    elif choice == 7:
        print("See borrowings")
        borrowing()
    else:
        print("Invalid option")
    print("-"*50 + "\n")

fun()
