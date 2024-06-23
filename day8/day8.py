import math

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def greet():
    print("asdasd")
    print("kolbasz")
    print("hogyér adod")

def greet_with_name(name):
    print(f"Szevasz, {name}")
    print("kolbasz")
    print("hogyér adod")

def paint_calc(height, width, cover):
    cans = height * width / cover
    cans = math.ceil(cans)
    
    print(f"{cans} doboz kell a festéshez")

def wall_paint():
    test_h = int(input("milyen magas a fal (m) ?    "))
    test_w = int(input("milyen széles a fal (m) ?   "))
    coverage = 5
    
    paint_calc(height=test_h, width=test_w, cover=coverage)  
    
def prime_checker(number):
    if number < 2:
        print("aazért inkább próbálj meg 1-nél nagyobb számot írni")
    if number < 4:
        print("prím")
        return
    if number % 2 == 0:
        print("nem prím")
        return
    for i in range (5, math.ceil(number / 2), 2):
        if number % i == 0:
            print("nem prím")
            return
    print("prím")

def ceaser(text, shift, direction):
    len_alphabet = len(ALPHABET)
    new_text = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        new_letter_place = ALPHABET.index(letter) + shift
        if abs(new_letter_place / len_alphabet) >= 1:
            new_letter_place = math.ceil(new_letter_place % len_alphabet) 
            
        new_text += ALPHABET[new_letter_place]
        
    print(f"ez a szó:   {new_text}")



def brutal_secret_caesar_cipher():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(text, shift, direction)
    

brutal_secret_caesar_cipher()


    