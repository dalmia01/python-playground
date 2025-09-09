# Exercise 3 - KBC
questions = ("What is the capital city of India?",
             "Who was the first President of independent India?",
             "In which year did India become a Republic?")
options1 = ("Kolkatta", "Mumbai", "Chennai", "Delhi")
options2 = ("Rajendra Prasad", "Jawaharlal Nehru", "Sardar Patel",
            "B. R. Ambedkar")
options3 = (1947, 1948, 1950, 1952)
options = (options1, options2, options3)
answers = (4, 1, 3)

print("""
Note: Before starting some instructions : 
1. answer only in 1,2,3,4
2. each correct answer will give you 100
3. as soon you give incorrect answer, game will be finished
""")


def playGame():
    userAnswers = []
    correctUserAnswers = []
    moneyWon = 0
    eachStepMoney = 100
    for questionIndex, questionItem in enumerate(questions):
        print("-----------")
        print(f'{questionItem} : ')
        print("Below mentioned are the options: ")
        for mainOptionIndex, mainOption in enumerate(options[questionIndex]):
            print(f"{mainOptionIndex + 1}. {mainOption}")
        answer = input("Choose you option : ").strip()
        userAnswers.append(answer)
        if (isinstance(answers[questionIndex], str)):
            if (answer.lower() == str(answers[questionIndex]).lower()):
                moneyWon = moneyWon + eachStepMoney
                correctUserAnswers.append(answer)
            else:
                print("Game Finished")
                break
        elif (isinstance(answers[questionIndex], int)
              and answer == str(answers[questionIndex])):
            moneyWon = moneyWon + eachStepMoney
            correctUserAnswers.append(answer)
        else:
            print("Correct answer was : ", answers[questionIndex], ".",
                  options[questionIndex][answers[questionIndex] - 1])
            print("Game Finished")
            break

    print("Total money you won : ", moneyWon)
    print("Total correct answers : ", len(correctUserAnswers))
    print("-----------------------")
    return


while (True):
    isPlay = input("Do you want to play the game (Y/N) : ").strip()
    if (isPlay.lower() == "yes" or isPlay.lower() == "y"):
        print("Thanks for accepting game, we will get you started soon: ")
        playGame()
    else:
        print(
            "No worries, may be next time you will be ready. Enjoy your day!!!"
        )
        break
