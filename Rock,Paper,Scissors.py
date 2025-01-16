import random
def choice(c):
    if c==1:
        choice="Rock"
    if c==2:
        choice="Paper"
    if c==3:
        choice="Scissors"
    return choice

print("RULES FOR ROCK, PAPER, SCISSORS GAME ")
print("1. Scissors vs Paper >>>>> Scissors wins ")
print("1. Rock vs Paper >>>>> Paper wins ")
print("1. Scissors vs Rock >>>>> Rock wins ")

while True:
    print()
    print("Choose your option: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    c=int(input("Enter your choice: "))
    if c<1 or c>3:
        print("Error: Invalid Choice")
        continue
    print()
    print("User's choice: ",choice(c))

    comp_c=random.randint(1,3)
    print("Computer's choice: ",choice(comp_c))

    print()
    if c==comp_c:
        print("<<<<<<<<<< It's a tie >>>>>>>>>>")
    elif (c==1 and comp_c==2) or (c==2 and comp_c==3) or (c==3 and comp_c==1):
        print("<<<<<<<<<< Computer Wins >>>>>>>>>>")
    elif (c==1 and comp_c==3) or (c==2 and comp_c==1) or (c==3 and comp_c==2):
        print("<<<<<<<<<< User Wins >>>>>>>>>>")

    print()
    x=input("Do you want to play again (Y/N) ?: ")
    if x=="N":
        break
print("Thank You for Playing")
          
    
