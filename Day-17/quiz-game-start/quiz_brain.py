
class QuizBrain:
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        
    
# TODO: asking the questions
    def next_question(self):
        current_question = self.question_list[self.question_number]
        input(f"Q.{self.question_number}: {}")

# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz
