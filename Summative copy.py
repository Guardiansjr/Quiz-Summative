
from tkinter import *
from tkinter import messagebox
import random
import time

#makes a list of countries from text file
with open('/Users/s210230/PycharmProjects/untitled1/Countries') as f:
        countries = f.readlines()
        countries = [x.strip() for x in countries]

#counts amount of countries you got correct
questionThreeCounter = 0

#counts your overall score
correctCounter = 0

#sets player name has blank
playerName = ""

def start():
    global playerName
#asks your name
    playerName = str(input("Why hello there! Welcome to the IMPOSSIBLE quiz. This is a KNOWLEDGE based game. KNOWLEDGE is POWER.  What is your name?"))
    print("Okay,", playerName, ", let's take you to question one")
    questionOne()

#when you lose, plays this function
def end():
    global playerName
    print("Your score has been added to the leaderboards.")

    #variable will be used to add score and playername to leaderboard
    leaderboardAppend = str(correctCounter) +" "+ playerName

    leaderboardFile = open('/Users/s210230/PycharmProjects/untitled1/Leaderboard','a')



    #adds score and playername to leaderboard
    leaderboardFile.write(leaderboardAppend)

    #makes a new line
    leaderboardFile.write("\n")

    leaderboardFile.close()

    #if they press 1, prints the leaderboard
    viewLeaderboard = int(input("To view leaderboard, press 1"))
    if viewLeaderboard == 1:
        with open('/Users/s210230/PycharmProjects/untitled1/Leaderboard') as f:
            leaderboardList = f.readlines()
            leaderboardList = [x.strip() for x in leaderboardList]

            sortedList = sorted(leaderboardList, reverse = True)
            print(sortedList)
    else:
        print("okay")

def questionOne():
    global correctCounter
    print("Okay, question 1. What of these is NOT a country?")
    answer = str(input("Georgia. Barama. Nauru. Dijibouti"))
    answer = answer.lower()

    #if answer is correct
    if answer == "barama":
        correctCounter = correctCounter + 1
        print("Hey! You got the question right! On to the next question!")
        questionTwo()

    #if answer not correct
    else:
        print("WRONG! GGWP . Your final score is" , correctCounter)
        end()

def questionTwo():
    global correctCounter
    answer = int(input("How many letters are there in the alphabet"))

    #if answer correct ("alphabet" has eight letters)
    if answer == 8:
        print("Woah, you got this correct? Okay, next question!")
        correctCounter = correctCounter+1
        questionThree()

    else:
        print("hah. you lose. final score:", correctCounter)
        end()

def questionThree():
    global questionThreeCounter
    global correctCounter

    #prints how many more countries you need to guess
    print(5-questionThreeCounter, "more to go!")

    answer = str(input("Name 5 countries without the letter A "))

    #if their answer is inside countries list and it is not their fifth guess
    if answer.lower() in countries and questionThreeCounter < 4:
        print("You got one country!")
        questionThreeCounter = questionThreeCounter + 1
        countries.remove(answer)
        questionThree()

    #if their answer is inside countries list and it is their fifth guess (meaning they completed the game)
    elif answer.lower() in countries and questionThreeCounter == 4:
        print("You got all the countries!")
        correctCounter = correctCounter + 1
        questionFour()

    #not in list, you lose
    else:
        print("You lost. Final score:", correctCounter)
        end()

def questionFour():
    global correctCounter
    print("Alright")
    answer = int(input("How many month(s) in a year has 28 days?"))

    #if answer is correct(all months have at least 28 days)
    if answer == 12:
        print("congrats, next question")
        correctCounter = correctCounter + 1
        questionFive()

    #if incorrect
    else:
        print("WRONG. Final score:", correctCounter)
        end()

def questionFive():
    global correctCounter
    answer = int(input("There are 5 apples, you take away 3, how many do you have now?"))

    #if answer is correct
    if answer == 3:
        print("correct! Next question")
        correctCounter = correctCounter + 1
        questionSix()

    #if incorrect
    else:
        print("You lose. Final score:" , correctCounter)
        end()

def questionSix():
    global continueQuestionSix

    #makes a window
    root = Tk()

    #adds a button on the window
    question = Button(root, text = "Look at me! I am a window now! Proceed to next question?", command = questionSixContinued)
    question.pack()
    root.mainloop()


#if they click the button, this function is run
def questionSixContinued():
    global correctCounter
    #makes a pop up
    messagebox.showinfo("I AM A WINDOW" , "Quick! What is the capitol of Luxembourg?")
    answer = str(input(""))

    #if answer is correct
    if answer.lower() == "luxembourg":
        print("You got it! Next question")
        questionSeven()

    #if answer is incorrect
    else:

        print("Aw, you lost! Final score:", correctCounter)
        correctCounter = correctCounter + 1
        end()

def questionSeven():
    global correctCounter

    #randomly selects the first number
    num1 = random.randint(1,10)

    #number will be used to add
    additionKey = random.randint(1,5)

    #number will be used to multiply
    multiplyKey = random.randint(1,3)

    #makes number 2
    num2 = (num1 + additionKey)*multiplyKey

    #makes number 3
    num3 = (num2 + additionKey)*multiplyKey

    #makes number list that has the three numbers in it
    numberList = [num1, num2, num3]

    print(numberList)
    print(additionKey)
    print(multiplyKey)

    answer = int(input("What is the next number in the sequence?"))

    #if their answer is correct
    if answer == (num3 + additionKey)*multiplyKey:
        print("Correct! Next question")
        correctCounter = correctCounter + 1
        questionEight()

    #if incorrect
    else:
        print("You lose. Final score:", correctCounter)
        end()

def questionEight():
    global correctCounter
    answer = int(input("What part of speech is 'Hello'? 1. Conjunction  2. Interjection  3. Noun  4. Verb"))

    #if correct
    if answer == 2:
        print("Correct! Next question")
        correctCounter = correctCounter + 1
        questionNine()

    #if incorrect
    else:
        print("Wrong! Final score:" ,correctCounter)
        end()

def questionNine():
    global correctCounter

    #counts how many words they typed in
    run = 0


    print("Alright, you got three seconds to type in every word.")

    #pauses for a moment
    time.sleep(5)

    #makes a list with all the lines of textfile inside the list
    with open('/Users/s210230/PycharmProjects/untitled1/Typing Test') as f:
        words = f.readlines()
        wordList = [x.strip() for x in words]

    #while it is less than their tenth run
    while run < 10:

        #sets the maximum time you can have to write in the word
        timeout = time.time() + 3

        #selects a word from the list of random words
        selectedWord = wordList[random.randint(1, 100-run)]

        #prints the word, player must type it
        answer = str(input(selectedWord))

        #if correct and the time is less than 3 seconds
        if answer == selectedWord and time.time()<timeout:
            run = run + 1
            wordList.remove(selectedWord)

        #if answer incorrect
        elif answer != selectedWord:
            print("Wrong Spelling. Final Score:", correctCounter)
            end()

        #if it took too long
        else:
            print("Too long! Final Score:", correctCounter)
            end()


    print('You did it!')
    correctCounter = correctCounter + 1
    questionTen()

def questionTen():
    global correctCounter
    print("Okay. Question 10")
    answer = str(input("What British plane in World War 2 was small, agile, and could out preform German planes?"))
    if answer.lower() == "spitfire":
        print("Correct!")
        correctCounter = correctCounter + 1
        questionEleven()

    else:
        print("wrong! Final score:" ,correctCounter)
        end()

def questionEleven():
    global correctCounter
    print("Good stuff. ")
    answer = int(input("what is the meaning of life? (hint: it is a number)"))
    if answer == 42:
        print("Correct!")
        correctCounter = correctCounter + 1
        questionTwelve()

    else:
        print("WRONG! Final score:" , correctCounter)
        end()


def questionTwelve():
    global correctCounter
    print("Good stuff. ")
    answer = int(input("What is 1/2 of 1/5 of 1/4 of 200? 1. 5    2. 10    3. 15   4. 20"))
    if answer == 1 or 5:
        print("Correct!")
        correctCounter = correctCounter + 1
        questionThirteen()

    else:
        print("That is wrong! Final score:" , correctCounter)
        end()



def questionThirteen():
    global correctCounter
    print("Good stuff.")
    answer = str(input("What does bible literally mean? a. Christian Book   b. Book of God   c. Religion Book   d. Holy Book"))
    if answer.lower() == "d" or "holy book":
        print("Correct!")
        correctCounter = correctCounter + 1
        questionFourteen()

    else:
        print("WRONG! Final score:" , correctCounter)
        end()


def questionFourteen():
    global correctCounter
    print("Good stuff.")
    answer = str(input("If all zoozies are loozies, and all loozies are foozies, are all zoozies foozies? True or false?"))

    if answer.lower() == "true":
        print("Correct!")
        correctCounter = correctCounter + 1
        questionFifteen()

    else:
        print("WRONG! Final score:" , correctCounter)
        end()


def questionFifteen():
    global correctCounter
    print("Good stuff. Last question!:")
    answer = int(input("Have you been paying attention to the question number? What question is this? 14? 15? 16? 17?)"))
    if answer == 15:
        print("Correct!")
        correctCounter = correctCounter + 1
        gameEnd()
    else:
        print("WRONG! Final score:" , correctCounter)
        end()

def gameEnd():
    print("Congragulations! You made it to the end! It was a long quiz, but you did it!")
    end()

#main code
start()
