import random
a=random.randint(1,20)
z=True
print("Hello! What is your name?")
b=input()
q=1
print("Well, "+b+", I am thinking of a number between 1 and 20.")
while z==True:
    y=input(" Take a guess.\n")
    x=int(y)
    if x==a:
        print("Good job, ",b ," You guessed my number in ",q, " guesses!")
        z=False
    elif x>a:
        print("Your guess is too high.")
        q+=1
    elif x<a:
        print("Your guess is too low.")
        q+=1