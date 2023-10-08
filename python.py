secret = "cat"
num = int(input("How many guesses would you like : "))
print("-------------------")
n = str(num)
o = num - 1
print("Guesses left : " + n)
guess = input("Guess the animal that I am thinking of : ")
for i in range(o,0,-1):
    if guess == secret:
        print("You won!")
        break
    elif guess != secret:
        print("Guesses left : " + str(i))
        print("Guess again! ")
        guess = input("Guess the word that I am thinking of : ")
if guess == secret:
    print("You won")
else:
    print("The word was " + secret + ".")

again = input("Would you like to play again (y or n) : ")
if (again == "y") or (again == "yes") or (again == "Y"):
    
    secret = "bird dog horse tiger"
    numguess = int(input("How many guesses would you like : "))
    print("-------------------")
    a = str(numguess)
    t = numguess - 1
    print("Guesses left : " + a)
    guess = input("Guess an animal in the phrase that I am thinking of : ")
    for i in range(t,0,-1):
        if guess in secret:
            break
        elif guess not in secret:
            print("Guesses left : " + str(i))
            print("Guess again! ")
            guess = input("Guess a word in the phrase that I am thinking of : ")
    if guess in secret:
        print("You won, the phrase was " + secret +"!")
    else:
        print("The phrase was '" + secret + "'.")

else:
    print("Goodbye!")
    