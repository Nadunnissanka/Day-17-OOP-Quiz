from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# question bank
question_bank = []
for question in question_data:
    question = Question(question["text"], question["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f"You completed the Quiz!\nYou got {quiz.score} / {quiz.question_number} correct!")
