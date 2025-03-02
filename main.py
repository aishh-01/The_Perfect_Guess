import random
n=random.randint(1,100)
a=-1
guessess=1
while(a!=n):
    a=int(input("Guess any number: "))
    if(a>n):
        print("Lower number please")
        guessess += 1
    elif(a<n):
        print("Higher number please")
        guessess += 1

print(f"You have guessed the number {n} correctly in {guessess} attempts")