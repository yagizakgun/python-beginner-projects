print("Welcome to my digital quiz")


playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Ok! Lets play game")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "cpu":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "gpu":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == "ram":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does PCU stand for? ")
if answer.lower() == "pcu":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("Your got " + str(score) + " questions correct!")
print("Your got %" + str((score / 4) * 100))
