import random
a=random.randint(1,10)
b=-1
guess=0
while (a!=b):
    b=int(input("please Guess the number:"))
    if b<0 or b>10:
        print("please enter the correct number and come to play again!")
        break
    if b>a:
        print(f"the numbre computer choose is {a} and you choose is {b}")
        print("please guess lower number!")
    elif b<a:
        print(f"the numbre computer choose is {a} and you choose is {b}")
        print("please guess a higher number!") 
    
    else:
        print(f"the numbre computer choose is {a} and you choose is {b}")
        print("you gussed it right bro!")
        break   
    guess+=1
    print(f"the number of guesses you took to guess the correct number {b} is : {guess}")

