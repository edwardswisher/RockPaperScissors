import random
# can import peudorandomness to your application
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#will choose a random int in the range specified, including the highest int


print("Welcome to Rock, Paper Scissors!")

userChoice = int(input("What do you choose? Type 0 for rock, 1 for Paper, or 2 for Scissors.\n "))



if userChoice == 0:
    print(rock)
    
elif userChoice == 1:
    print(paper)
    
else:
    print(scissors)

computerChoice = random.randint(0,2)
computerChoice2 = print("the computer chose")
if computerChoice == 0:
    print(rock)
    
elif computerChoice == 1:
    print(paper)
    
elif computerChoice == 2:
    print(scissors)
else:
    print("Oops")
    
if userChoice == computerChoice:
    print("You tied!")
elif userChoice == 0 and computerChoice == 1:
    print("You Lose!")
elif userChoice == 1 and computerChoice == 2:
    print("You Lose!")
elif userChoice == 2 and computerChoice == 0:
    print("You Lose!")
elif userChoice == 0 and computerChoice == 2:
    print("You Won!")
elif userChoice == 1 and computerChoice == 0:
    print("You Won!")
elif userChoice ==2 and computerChoice ==1:
    print("You Won!")  
    
    
input()