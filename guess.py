def new_game():
    guesses = []
    correct_guess = 0
    question_num = 0

    for key in questions:
        print(key)
        for i in options[question_num]:
            print(i)
        guess = input("Enter A, B, C or D: ").upper()
        guesses.append(guess)
        print("----------------------------------------")
        question_num+=1

        correct_guess += check_answers(questions.get(key), guess)

    display_score(correct_guess, guesses)


def check_answers(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

def display_score(correct_guess, guesses):
    print("ANSWERS: ",end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("GUESSES: ",end="")
    for i in guesses:
        print(i,end=" ")
    print()
    
    score = int((correct_guess/len(questions))*100)
    print("Your score is: "+str(score)+"%")

def play_again():
    query = input("Do you want to play again yes/no: ").upper()
    if query == "YES":
        return True
    else:
        return False


questions = {
    "What is the full meaning of JSON?: " : "A",
    "What color is the sky?: " : "C",
    "Who is Albert Einstein?: " : "D",
    "Where is Nigeria located?: " : "B"
}

options = [["A. Java Script Object Notation","B. JQUERY Script Object Notation","C. James Science Observer Night","D. Junior Scene On"],
["A. Red","B. White","C. Blue","D. Indigo"],
["A. Doctor","B. Botanist","C. Wife","D. Scientist"],
["A. Europe","B. Africa","C. Asia","D. America"]]

new_game()
while play_again():
    new_game()
else:
    print("Byee")
