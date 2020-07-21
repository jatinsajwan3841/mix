from datetime import datetime
from datetime import timedelta

def calc():
    new=100-age
    new=new*365
    print("Okay "+ name + ", so you will turn 100 on : ")
    print (datetime.now() + timedelta(days=new))

name=str(input("your name please"))

while True:
    try:
        age=int(input("your age please"))
        break
    except ValueError:
        print("No valid integer! Please try again ...")


while True:
    try:
        chc = str(input("wanna know when you will turn 100? \n enter Y or N only."))
        if chc == "y" or chc == "Y":
            calc()
            break

    except:
        print("Please " + name + ", enter right input")

    else:
        if chc == "n" or chc == "N":
            exit("Okay " + name + ", ending program")

print("present datetime : ")
print(datetime.now())
