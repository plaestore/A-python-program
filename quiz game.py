print("Welcome to my quiz game weebs!!")

playing = input("Would you like to play? ")
score = 0
if playing.lower() != "yes":
    quit()

    
print("Great!! lets play.")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct! You a genius :)")
    score += 1
else:
    print("Incorrect! Dumb")

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print("Correct! You a genius :)")
    score += 1
else:
    print("Incorrect! Dumb")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct! You a genius :)")
    score += 1
else:
    print("Incorrect! Dumb")

answer = input("What does STD stand for? ")
if answer.lower() == "standard":
    print("Correct! You a genius :)")
    score += 1
else:
    print("Incorrect! Dumb")

    
print("You had" +  str(score) + " questions correctly")
print("Your score is " + str((score/4) * 100) + "%")
