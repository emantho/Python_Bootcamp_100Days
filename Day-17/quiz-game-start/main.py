from os import system

from quiz_brain import QuizBrain; system("clear")
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain 

# TODO-2 Creating list objects -> creating question bank
question_bank = []

for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the Quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")