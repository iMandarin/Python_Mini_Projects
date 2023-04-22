print("Welcome to the quiz Game!")

playing = input("Do you want to play? ")
 #print(playing)

#for upper case letters.
#if playing.upper() != "YES":
# upper() will convert the string given to upper case letters.
#    quit()

#for lower case letters.
if playing.lower() != "yes":
#lower() will convert the string given to lower case letters.
    quit()

print("Okay! Let's play:)")
score = 0

answer = input("1. What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer = input("2. What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("3. What does RAM stands for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what does PSU stands for? ")
if answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!" )
print("You got " + str((score/4)* 100) + "%." )
