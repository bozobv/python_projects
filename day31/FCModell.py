import pandas as pd
import random

class FCModell:

    def __init__(self, input_filename): 
        #df_words = pd.read_csv(input_filename)      
        try:
            df_words = pd.read_csv(input_filename)
        except FileNotFoundError:
            df_words = pd.read_csv("day31/data/en-hun.csv")
        
        self.language_1 = df_words.columns[0]
        self.language_2 = df_words.columns[1]
        
        self.words = df_words.to_dict(orient="records")

        self.order_word = [number for number in range(len(self.words))]  
        random.shuffle(self.order_word) 
        
        self.current_iteration = -1     
        self.wrongs_order = []     
    
    def correct_answer(self):
        self.next_word()
    
    def incorrect_answer(self):
        if self.current_iteration >= 0 and self.current_iteration < len(self.order_word):
            self.wrongs_order.append(self.order_word[self.current_iteration])
        self.next_word()
    
    def next_word(self):
        self.current_iteration += 1
        
    def ended(self): 
        if(self.current_iteration >= len(self.order_word)):
            if not self.wrongs_order:
                return True
            else:
                self.current_iteration = 0
                self.order_word = self.wrongs_order
                self.wrongs_order = []
        return False     
    
    def get_word_language_1(self):
        return self.words[self.order_word[self.current_iteration]][self.language_1]
    
    def get_word_language_2(self):
        return self.words[self.order_word[self.current_iteration]][self.language_2]
    
    def get_language_1(self):
        return self.language_1
    
    def get_language_2(self):
        return self.language_2
    
    def save(self):
        words_to_learn = [
                        self.words[numth]
                        for i, numth in enumerate(self.order_word)
                        if numth in self.wrongs_order or i >= self.current_iteration
                        ]

        #azok a szavak kellenek, amelyeknek a száma benne van a wrongs order-ben, és amiknek a sorszáma nagyobb, mint a current_iteration
        data = pd.DataFrame(words_to_learn)
        data.to_csv("day31/data/words_to_learn.csv", index=False)