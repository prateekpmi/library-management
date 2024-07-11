from datetime import datetime
import mysql.connector
mydb =mysql.connector.connect(host='localhost',user='root',password='jan2008lucknow',database='libraryn') 
mycursor=mydb.cursor()

def addmember():
        member=input('enter a member in addMember - ')
        print(member)
        member_id=int(input('enter memberid - '))
        name=input('enter member - ')
        phoneno=int(input('enter phonenumber - '))
        email=input('enter email - ')
        address=input('enter address - ')
        current_datetime=datetime.now()

        query = "INSERT INTO MEMBERS (member_id, join_date, name, email, address) VALUES (%s, %s, %s, %s, %s)"
        values = (member_id, current_datetime, name, email, address)

        mycursor.execute(query, values)
        mydb.commit()
        print('done')


                                                             
def addbook():
        addbook=input('enter bookname - ')
        print(addbook)
        book_id=int(input('enter bookid - '))
        title=input('enter title - ')
        author=input('author name - ')
        genre=input('enter genre of book - ')
        isbn=int(input('enter isbn - '))
        publication_year=int(input('enter publication year - '))
        status=input('enter status of book - ')
        query1="INSERT INTO BOOKS(bookid,title,author,genre,isbn,publication_year,status) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        values1=(book_id,title,author,genre,isbn,publication_year,status)
        mycursor.execute(query1,values1)
        mydb.commit()
        print('done!')


def borrowbook():
        borrowbook=input('enter borrowbook - ')
        print(borrowbook)
        borrowing_id=int(input('enter borrowing id - '))
        book_id=int(input('enter book id - '))
        member_id=int(input('enter member id - '))
        fine=int(input('enter fine - '))
        join_date_str=input('Enter join date (YYYY-MM-DD) - ')
        join_date = datetime.strptime(join_date_str, '%Y-%m-%d')
        query2="INSERT INTO BORROWING(borrowing_id,book_id,member_id,fine,borrow_date) VALUES(%s, %s, %s, %s,%s)"
        value2=(borrowing_id,book_id,member_id,fine,join_date)
        mycursor.execute(query2,value2)
        mydb.commit()
        print('done!!')

def returnbook():
        returnbook=input('enter returnbook')
        print(returnbook)
        
        borrowing_id=int(input('enter borrowing id - '))
        book_id=int(input('enter book id - '))
        member_id=int(input('enter member id - '))
        returning_id=int(input('enter returning id - '))
        fine=int(input('enter fine - '))
        join_date_str1=input('Enter join date (YYYY-MM-DD) - ')
        join_date1= datetime.strptime(join_date_str1, '%Y-%m-%d')

        query3="UPDATE BORROWING SET RETURN_DATE=%s WHERE BORROWING_ID=%s"
        values3=(join_date1,borrowing_id)
        mycursor.execute(query3,values3)
        mydb.commit()
        print("done!!!")

def fun():
    choice=int(input('enter any choice- in fun'))
    if choice==1:
        addmember()
    elif choice==2:
        addbook()
    elif choice==3:
        borrowbook()
    elif choice==4:
        returnbook()
    else:
        print('invalid option - ')
fun()

    

    