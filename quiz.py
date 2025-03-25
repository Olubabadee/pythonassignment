#Simple Quiz Game 🎮
#Create a multiple-choice quiz with questions about Python, movies, or any fun topic! Display scores at the end and allow the user to play again. 🏆

# Store the questions 
questions = [
    "What is Python primarily used for?",
    "Which of the following is immutable in Python?",
    "What keyword is used to define a function in Python?",
    "Which data type is used to store multiple values in one variable?",
    "What does OOP stand for?"
]

options = [
    ["A) Web development", "B) Data Science", "C) Automation", "D) All of the above"],
    ["A) List", "B) Dictionary", "C) Tuple", "D) Set"],
    ["A) func", "B) define", "C) def", "D) function"],
    ["A) String", "B) Integer", "C) List", "D) Boolean"],
    ["A) Object-Oriented Programming", "B) Object-Orbit Processing", "C) Online Ordered Processing", "D) Open Object Protocol"]
]

answers = ["D", "C", "C", "C", "A"]

score = 0

# message = input(questions[0])

# for i in range(len(questions)):
#    print(questions[i])
#    for option in options[i]:
#       print(option)
for i in range(len(questions)):  # Loop through questions
    print(questions[i])  # Display the question
    
    for option in options[i]:  # Loop through the corresponding options
        print(option)  # Display options

    answer = input("Your answer: ")

    if answer == answers[i]:
        score +=1
   
    print(f"your score is {score} out of {len(questions)}")