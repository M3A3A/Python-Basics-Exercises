names = ["Mousa","Ali","Eisa","Mohammed"]
marks = [97,93,86,100]
ages = [19,26,24,17]

search = "search"
add = "add"



while True :
    ask = str(input("What Do You Want To Do : "))

    if ask == str("search") :
                x = int(input("Enter The ID Of Student : "))
                print ("=========================================")

                for i in range (len(names)) :
                    if i+1 == x :
                        print (f"The ID Of Student : {x}")
                        print ("The Name Of Student : ", names[i])
                        for j in range (len(ages)):
                            if j+1 == x :
                                print ("The Age Of Student : ", ages[j])
                        for m in range (len(marks)) :
                            if m+1 == x :
                                print ("The Mark Of Student : ", marks[m])
                print("=========================================")

    elif ask == str("add") :
                print("=========================================")
                n = str(input("Enter The Name of New Student : "))
                names.append(n)
                m = int(input("Enter The Mark of New Student : "))
                marks.append(m)
                a = int(input("Enter The age of New Student : "))
                ages.append(a)
                ID = len(names)
                print("The ID Of New Student : ", ID)
                print("=========================================")

    elif ask == str("check") :
            x = int(input("Enter The ID Of Student : "))
            print ("=========================================")
            for i in range (len(names)) :
                if (x == i+1) :
                        print ("=========================================")
                        print("The Student Actualy Vaild")
                        print ("=========================================")
                        print("The name of Student : ",names[i])
                        print("The age of Student : ",ages[i])
                        print("The mark of Student : ",marks[i])
                        print ("=========================================")
                else :
                      print ("The Student Isn't found (invaild)")


    


