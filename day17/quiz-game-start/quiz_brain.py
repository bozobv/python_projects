

class QuizBrain:

    def __init__(self, input_list):
        
        self.points = 0
        self.question_number = 0
        self.question_list = input_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
            

    def next_question(self):
        answer = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False):  ")

        self.check_answer(answer=answer, correct_answer=self.question_list[self.question_number].answer)
        
        self.question_number += 1


    
    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("fasza vagy, kitaláltad! Nyomjad tovább!!")
            self.points += 1
            return True 
        
        print(f"Nem volt jó :P No problemo, veressük tovább!!")
        
        return False

