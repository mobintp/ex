print("welcome to my computer game!")

playing = input("do you want to play?(Y/N): ")

if playing[0].lower() != "y":
    quit()
    
print("Okay! let's play :)")

answer = input("what does CPU stands for? ")

if answer == "centeral processing unit":
    print("correct!")
else:
    print("incorrect!")