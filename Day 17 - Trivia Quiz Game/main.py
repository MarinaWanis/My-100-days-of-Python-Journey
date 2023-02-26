from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data["results"]:
    question_object = Question(question["question"], question["correct_answer"])
    question_bank.append(question_object)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You have completed the quiz")
print(f"Your final score: {quiz_brain.score}/{quiz_brain.question_number}")
