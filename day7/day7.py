import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

hangman_logo = """_                                             
                 | |                                            
                 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
                 | '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
                 | | | | (_| | | | | (_| | | | | | | (_| | | | |
                 |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                                     __/ |                      
                                    |___/                       """

WORD_LIST = ["kolbász", "mókus", "kutya", "ananász", "százlábú", "elem", "orrszarvú", "fájdalom", "fos", "förtelmes", "húgy", "haszontalan",
             "undoritó", "kula", "megalkuvás", "elég", "soha", "több", "ilyet", "nem", "akar", "lát", "itt", "ennél", "jobb", "lesz"]

def generate_word():
    return random.choice(WORD_LIST)

def check_guess(letter, word):
   
    pass

def wrong_guess(fails_remain):
    if ( 0 >= fails_remain):
        print("vesztettél :P")
        return True
    return False

def print_display(display):
    for i in display:
        print(i, end = " ")
    print()
        
def update_display(guess, display, word):
    for i in range(0, len(word), 1):
        if guess == word[i]:
            display[i] = guess
    return display     

def print_hangman(hp):
    print(stages[hp])   

def hangman():
    
    chosen_word = generate_word()
    print(hangman_logo)
    print("üdv a csidi-csodajó akasztófa játékunkban")
    
    guessed_leters = []
    
    leters_remain = set(chosen_word)
    hp = 6
    display = []
    for _ in range (len(chosen_word) ):
        display.append('_')
         
    
    
    ended = False
    while (ended != True):
        print_display(display)
        
        print_hangman(hp)
        
        guess = input("tippelj meg EGY betűt ebbúl, teswérem    ").lower()
        
        if len(guess) != 1:
            print("Nagy betűvel irtam, hogy EGGGGGGGY betű, na, próbáljuk ujra")
        elif guess in guessed_leters:
            print("ez a betű már vótmá, próbáld újra")
        else:
            guessed_leters.append(guess)
            if guess in leters_remain:
                leters_remain.remove(guess)
                print("BENNE VAN, NAON JÓ VAGY")
                display = update_display(guess, display, chosen_word)
                if not leters_remain:
                    ended = True
                    print("GYŐZTÜNK")
            else:
                print("nincs benne :P")
                hp -= 1
                ended = wrong_guess(hp)
        

            
                
        pass
    
    
    print_hangman(hp)

    print("a játéknak vége!!")

    

hangman()