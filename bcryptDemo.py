import bcrypt
import random

userArr = []
streak = 0



def guessGame():
    global streak
    if userArr:
        arrSize = len(userArr)
        randomNum = random.randint(0, arrSize-1)
        randomUser = userArr[randomNum][0]
        randomUserPass = userArr[randomNum][1]
        result = False
        numTries = 0
        while not result and numTries < 5:
            guessPass = input("Can you try guessing the password for {}: ".format(randomUser))
            numTries = numTries + 1
            encodedGuess = guessPass.encode('utf-8')
            result = bcrypt.checkpw(encodedGuess, randomUserPass)
        if numTries > 4:
            print("Too many attempts.")
            print("You had a streak of ", streak)
            exit()
            regAgain()
        elif numTries == 1:
            print("You guessed the password correctly in 1 try!")
            streak = streak + 1
            print("Your streak is: ", streak)
            regAgain()
        else:
            print("You guessed the password correctly in ", numTries, " tries!")
            streak = streak + 1
            print("Your streak is: ", streak)
            regAgain()

def register():
    

    
    user = input("Enter a username: ")
    if user in [data[0] for data in userArr]:
        print("Username taken")
    else:
        print("Thank you", user,".\n")
    #print(userArr)

    password = input("Enter a password: ")
    encodedPw = password.encode('utf-8')

    salt = bcrypt.gensalt()
    hashpass = bcrypt.hashpw(encodedPw, salt)

    userAndPass = [user, hashpass]
    userArr.append(userAndPass)
    guessGame()
    #print(userArr)


def regAgain():
    global streak
    choice = int(input("Enter 1 to register another user! Enter 0 to give up!"))
    if(choice == 1):
        register()
    else:
        print("You had a streak of ", streak)
        with open('userAndPass.txt', 'w') as file:
            for data in userArr:
                file.write(f"{data[0]}:{data[1]}\n")
        exit()
    



doReg = 45
while(doReg != 1 or 0 or 2):
    doReg = int(input("Do you want to register? 1 for yes 0 for no. Type 2 to load userAndPass.txt: "))

    if(doReg == 1):
        register()
    elif(doReg == 0):
        print("Exiting")
        exit()
    elif(doReg == 2):
        
        with open('userAndPass.txt', 'r') as file:
            lines = file.readlines()
            userArr = [line.strip().split(':') for line in lines]
            userArr = [[data[0], data[1].encode('utf-8')] for data in userArr]
        guessGame()
    else:
        print("Enter 1 or 0.")


    
        
        
    

