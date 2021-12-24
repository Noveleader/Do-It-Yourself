from data import question_data
import quiz_brain
from quiz_brain import calculate_score

for _ in range(len(question_data)):
    quizess=calculate_score()
    quizess.quiz()
    quizess.score_tracker()
    print()

print("You have completed the quiz!!")
print(f"Your final score was: {quiz_brain.user_score}/{quiz_brain.total_score}")