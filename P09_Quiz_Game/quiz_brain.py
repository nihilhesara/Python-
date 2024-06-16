class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
    
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            False
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q{self.question_number}. : {current_question.text} (True/False) : ")