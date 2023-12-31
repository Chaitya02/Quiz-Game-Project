class QuizBrain:

    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_no < len(self.question_list):
            return True
        return False

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_ans = input(f"Q.{self.question_no}: {current_question.text} (True/False)?: ")
        self.check_answer(user_ans, current_question.answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer was {correct_ans}.")
        print(f"Your current score: {self.score}/{self.question_no}")
        print("\n")
