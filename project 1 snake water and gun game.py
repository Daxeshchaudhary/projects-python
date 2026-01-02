
print(""" ** read this instructions     **
      1=snake
     -1 for water
      0 for gun""")
import random
a=random.randint(-1,1)
n=int(input("Enter your number:"))
print("the number chosen by compter is:",a)
if a==n:
    print("it is an draw!")
else:
    if a==1 and n==-1:
        print("computer wins!, snake drinks water!")


    elif a==-1 and n==1:
        print("you win!, snake drinks water!")


    elif a==-1 and n==0:
        print("computer wins!,water drains gun!")

    elif a==0 and n==-1:
        print("you win!,water drains gun!")

    elif a==1 and n==0:
        print("you win!,gun shoots snake!")

    elif a==0 and n==1:
        print("computer wins!,gun shoots snake!")

    else:
        print("number is wrong!")


