import random 

def guess(x):
    random_number = random.randint(1, x + 1)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess a number: "))
        
        if guess < random_number:
            print("Try again! guess a bigger number!")
        elif guess > random_number:
            print("Try again! guess a smaller number!")

    print(f"yay! you guessed the {random_number}, congrats!")
        
        
guess(100)        
