'''while True:
    try:
        n=int(input("Enter an First Integer"))
        m=int(input("Enter an second Integer"))
        z=n/m
        break
    except Exception as e:
        print("Not an Integer! Please enter again")
        print(e)
    except ValueError:
        print("Not an Integer ")
    finally:
        print("You Successfully Entered an Integer ")'''
try:
    klu1 = open("file.txt","w+")
    try:
        klu1.write("its a file handling ")
    finally:
        klu1.close()
except IOError:
    print("file not found")
else:
    print("The file opened successfully")
    klu1.close()