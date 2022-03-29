from os import system

from quiz_brain import QuizBrain; system("clear")
from question_model import Question
from data import question_data

# TODO-2 Creating list objects -> creating question bank
question_bank = []

#for i in range(len(question_data) - 1):
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

print(question_bank[0].text)

QuizBrain(question_bank)
