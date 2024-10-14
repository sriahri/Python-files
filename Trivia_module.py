class Question:
    def __init__(self, question, answer1, answer2, answer3, answer4, solution):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.solution = solution

    def get_question(self):
        return self.question

    def get_answer1(self):
        return self.answer1

    def get_answer2(self):
        return self.answer2

    def get_answer3(self):
        return self.answer3

    def get_answer4(self):
        return self.answer4

    def get_solution(self):
        return self.solution

    def set_question(self, question):
        self.question = question

    def set_answer1(self, answer1):
        self.answer1 = answer1

    def set_answer2(self, answer2):
        self.answer1 = answer2

    def set_answer3(self, answer3):
        self.answer1 = answer3

    def set_answer4(self, answer4):
        self.answer1 = answer4

    def set_solution(self, solution):
        self.solution = solution

    def __str__(self):
        return '{}\nOptions\n{}\n{}\n{}\n{}\n'.format(self.question, self.answer1, self.answer2, self.answer3, self.answer4)
