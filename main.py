def addmember():
        member=input('enter a member in addMember')
        print(member)

def addbook():
        addbook=input('enter bookname')
        print(addbook)

def borrowbook():
        borrowbook=input('enter borrowbook')
        print(borrowbook)

def returnbook():
        returnbook=input('enter returnbook')
        print(returnbook)

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


    

    