from data import question_data

class ask_question:
    number=0

    def __init__(self):
        self.questions=question_data[self.number]["question"]
        user_input=input(f"Q.{self.number+1}: {self.questions} (True/False) ")
        self.user_answers=user_input.title()