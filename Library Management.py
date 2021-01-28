def library():
    print ("Whoch books you want to go with?")

    print ()

    print ("Press 1 for Essential of Artificial Intelligence and 2 for Employability Skills")
    a = str (input ("Enter-> "))

    if a == '1':
        print ("Thank you for going with Essentials of Artificial Intelligence!")
    elif a == '2':
        print ("Thank you for going with Employability Skills")
    else:
        print ("Invalid Input")
        quit()
    print ("What do you want to do?")
    print ("Press 1 for Rent the Book")
    print ("Press 2 for Buy the Book")
    print ("Press 3 for Read the Book")
    print ("Press 4 for returning the Book")

    b = str (input ("-> "))
    print ()

    if b == '4':
        print ("Thank you for returning the book!")
        print ("Please visit again!")
    elif b == '1':
        print ("Thank you very much, Please pay at the Counter!")
        if a == '1':
            cost = 50
        elif a == '2':
            cost = 40
        print ("Your bill is of Rs.", cost)
    elif b == '2':
        print ("Thank you for buying the book! Please pay at the Cash Counter and don't forget to take the bill!")
        if a == '1':
            cost = 395
        elif a == '2':
            cost = 200
        print ("Your bill is of Rs.", cost)
    elif b == '3':
        print ("You may read the book! Have fun")
        if a == '1':
            cost = 25
        elif a == '2':
            cost = 20
        print ("Your bill is of Rs.", cost)
    else:
        print ("Invalid Input")
    
    print ()

library()
while True:
    print ()
    print ("Do you want to reuse the application?")
    print ("Press 1 for yes and 2 for no")
    h = str (input ("-> "))

    if h == '1':
        print ()
        library()
    elif h == '2':
        print ("Thank you for using the application!")
        break
    else:
        print ("Invalid Input")
        print ()