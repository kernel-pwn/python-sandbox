

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A.116","B.117","C.118","D.119"),
           ("A.whale","B.crocodile","C.elephant","D.ostrich"),
           ("A.nitrogen","B.oxygen","C.co2","D.hydrogen"),
           ("A.206","B.207","C.208","D.209"),
           ("A.mercury","B.venus","C.earth","D.mars"))

answers = ("C","D","A","A","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your guess: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
        print(f"{answers[question_num]} was the correct answer.")
    question_num += 1

print("------------------")
print("      Result      ")
print("------------------")

print("answers: ", end="")
for answer in answers:
    print(answer)

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

print(f"your score is {score}")
score = int(score / len(questions) * 100)
print(f"your score is: {score}%")