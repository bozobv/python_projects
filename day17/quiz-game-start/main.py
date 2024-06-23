from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    question_bank.append(Question(data["text"], data["answer"]))

qb = QuizBrain(question_bank)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
while qb.still_has_questions():
    qb.next_question()

print("Elvégezted a quizt ;)")
print(f"\n\n\n\nA VÉGEREDMÉNYED {qb.points}/{len(question_bank) }\n\n\nÜgyes cica vagy ;)")