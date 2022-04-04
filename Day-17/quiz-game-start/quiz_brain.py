
from question_model import Question


class QuizBrain:
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        
# TODO: PART 4 - Create a loop to keep asking until the end of list
    def still_has_questions(self):
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False
         
        ## 👆This expression can be more shorter👇
        return self.question_number < len(self.question_list)

# TODO: asking the questions
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer) # self it's not included as argument but yes as parameter👇
        

# TODO: PART 5 - checking if the answer was correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You get it right!")
            
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

# TODO: checking if we're the end of the quiz
