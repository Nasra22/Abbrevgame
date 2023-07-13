print("Welcome to the quiz game!")

playing = input("Do you want to proceed with the game?")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play!")

answer = input("What does RAM stand for?")
if answer.lower() == "random access memory":
    print('Correct!')
else:
    print("Incorrect!")

answer = input("What does ALU stand for?")
if answer.lower() == "arithmetic logic unit":
    print('Correct!')
else:
    print("Incorrect!")
answer = input("What does HTML stand for?")
if answer.lower() == "hypertext markup language":
    print('Correct!')
else:
    print("Incorrect!")

answer = input("What does IP stand for?")
if answer.lower() == "internet protocol":
    print('Correct! Nice work')
else:
    print("Incorrect!")

    answer = input("What does SSD stand for?")
if answer.lower() == "solid state drive":
    print('Correct! A genius I can say!')
else:
    print("Incorrect!")

answer = input("What does CPU stand for?")
if answer.lower() == "central processing unit":
    print('Correct!')
else:
    print("Incorrect!")

answer = input("What does BIOS stand for?")
if answer.lower() == "basic input output system":
    print('Correct! This is brilliant!')
else:
    print("Incorrect!")

answer = input("What does PC stand for?")
if answer.lower() == "personal computer":
    print('Correct!')
else:
    print("Incorrect!")

answer = input("The last one....What does OS stand for?")
if answer.lower() == "operating system":
    print('Correct! Hurray!!!You made it to the end!')
else:
    print("Incorrect!")