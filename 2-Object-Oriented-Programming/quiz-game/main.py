from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

# Fills question_bank with Question objects produced from questin_data
for i in question_data:
    question_bank.append(Question(i['question'], i['correct_answer']))

# Creates QuizBrain object with Question objects list question_bank
quiz = QuizBrain(question_bank)

# Starts questions
quiz.next_question()

# Checks if there are still questions and calls next
while quiz.still_has_questions():
    quiz.next_question()

# Final message
print(f'Finished! Your final Score is {quiz.score}, you answered correctly'
      f' {round(100 * quiz.score / len(quiz.questions_list))}% of all questions')