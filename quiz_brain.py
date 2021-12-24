from typing import AsyncIterable
from question_model import ask_question
from data import question_data
user_score=0
total_score=0
class calculate_score: 
    def quiz(self):
        global user_score
        global total_score
        total_score+=1
        quiz_start=ask_question()

        if quiz_start.user_answers==question_data[quiz_start.number]["correct_answer"]:
            print("Yes, you are correct.")           
            user_score+=1
            print(f"The correct answer was: {question_data[quiz_start.number]['correct_answer']}.")
            ask_question.number+=1
            
        else:
            print("Sorry that's wrong.")
            print(f"The correct answer was: {question_data[quiz_start.number]['correct_answer']}.")   
            ask_question.number+=1
            
    def score_tracker(self):
        print(f"Your score is: {user_score}/{total_score}")
    
    
