class QuizBrain:

    # Starts with at question_number and score at 0 with a list of Question objects input
    def __init__(self, questions):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions

    # Checks if the list still has any questions
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    # Checks if the answer input is correct
    def check_answer(self, user_answer, current_answer):
        if user_answer == current_answer:
            self.score += 1
            print(f'Correct! Score is {self.score}')
        else:
            print(f'Wrong! Score is still {self.score}')

    # Pulls next question and asks for answer, uses check_answer and updates question_number for next question
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)?: ").capitalize()
        self.check_answer(answer,current_question.answer)
        self.question_number +=1

