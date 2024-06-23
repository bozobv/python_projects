import time

class FCController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        language_1 = model.get_language_1()
        language_2 = model.get_language_2()

        self.view.set_languages(language_1, language_2)
        self.view.set_new_words("Press button to start", "Press a button for start")
        self.view.update_word_language_1()
        
    def correct_press(self):
        self.model.correct_answer()
        self.next_word()
     
    def incorrect_press(self):
        self.model.incorrect_answer()
        self.next_word()
        
    def next_word(self):
        if self.model.ended():
            self.view.next_words("VÉGEEE", "MEGTANULTAD")
            self.view.set_languages("VÉGEZTÉL, BARÁTOM", "VÉGEZTÉL, :P")
            self.view.update_word_language_1()
            return
        
        word_language_1 = self.model.get_word_language_1()
        word_language_2 = self.model.get_word_language_2()
        
        self.view.next_words(word_language_1, word_language_2)
        
    def save(self):
        self.model.save()
