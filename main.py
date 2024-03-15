import requests
import json

print("Welcome to the sports quiz !!!")
print("\n\n The rules of the game are, MCQ format will be followed; just put in the correct option as the input like :- a or b or c, etc. The options will be displayed on the screen along with the question")

print("\n\n")

response = requests.get("https://the-trivia-api.com/v2/questions")
data_retrieved = response.content

# Use json.loads to parse JSON data
data_retrieved = json.loads(data_retrieved)

asked = 0
userPoints = 0

totalQuestions = 10

if len(data_retrieved) > 0:
    while asked != 10:
        for qset in data_retrieved:
            question = qset['question']['text']
            print(f'\n\nQuestion :- {question}')   
            options = []
            print()
            options.extend(qset["incorrectAnswers"])
            options.append(qset["correctAnswer"])

            IndexNo = ['a', 'b', 'c', 'd']

            for op in options:
                print(str(IndexNo[options.index(op)]) + ")",op)

            userAnswer = input("Please enter the correct option: ")

            if options[IndexNo.index(userAnswer)] == qset["correctAnswer"]:
                print("Hurrah !, the correct answer you get a point.")
                userPoints += 1

            else:
                print("Oh No! Incorrect answer, better luck next time !!")

            asked += 1 

print("\n\nQuiz Over !!!!")
print("\n\n\n\nYou got a total points of " + str(userPoints) + " out of " + str(totalQuestions) + "points")