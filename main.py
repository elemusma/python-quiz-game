from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question['text']
    answer = question['answer']
    new_question = Question(text, answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
else:
    quiz.completed_quiz()
# quiz_brain
# quiz_brain.next_question('text','answer')

# QuizBrain(question_bank)
# QuizBrain(question_bank).next_question(question_bank)
# print(question_bank)

# length_of_data = len(question_data) - 1

# keep_answering = True
# question_number = 0
# score = 0
# index = question_number - 1

# while index < length_of_data:
#     question_number += 1
#     index += 1
#     # random_int = random.randint(0, length_of_data)
#     rand_text = question_data[index]['text']
#     rand_answer = question_data[index]['answer'].lower()
#     new_question = Question(rand_text, rand_answer)


#     question = input(f"Q.{question_number}: {rand_text} ").lower()

#     if question == rand_answer:
#         print("You got it right")
#         score += 1
#     elif question == 'exit':
#         keep_answering = False
#     else:
#         print("That's wrong.")

#     print(f"The correct answer was: {rand_answer.capitalize()}")
#     print(f"Your current score is: {score}/{question_number}")
# else:
#     print("\n")
#     print("You've completed the quiz.")
#     print(f"Your final score was {score}/{question_number}")
