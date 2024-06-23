import day14_art 
from game_data import data
import random

##higher or lower: kinek van több követője, név, leírás, ország, követőszám

def print_option(element):
    print(f"{element['name']}, aki {element['description']}, egyenesen innen: {element['country']}")

def compare(A, B, choice):
    print(f"az A: {A['follower_count']}")
    print(f"A B: {B['follower_count']}")

    if A['follower_count'] > B['follower_count']  :
        return choice == 'a'
    else:
        return choice == 'b'

def game():
    day14_art.print_logo()
    ongoing = True
    while ongoing:
        print("Kinek van több követője? Olvasd el és döntsd el!!!")

        succes = True
        win_counter = 0
        option_A = random.choice(data)
        data.remove(option_A)

        while succes:
            
            option_B = random.choice(data)
            data.remove(option_B) 

            print("\nAz A opció:\n")
            print_option(option_A)
            day14_art.print_vs()
            print("\nA B opció:\n")
            print_option(option_B)

            choice = input("Melyiknek van több követője? 'A' vagy 'B'??    ").lower()
            while choice != 'a' and choice != 'b':
                choice = input("Na ezt most próbáljuk újra. 'A' vagy 'B'?   ").lower()
            
            succes = compare(A=option_A, B=option_B, choice=choice)
            if succes:
                win_counter += 1
                if choice == 'b':
                    option_A = option_B
                print(f"Eddig {win_counter} menetet nyertél. Gyerünk tovább!!")

        print(f"Lúzer! {win_counter} menetet sikerült nyerned.")

        go_again = input("még egy kör? 'i' ha igen, 'n', ha nem   ").lower()
        while go_again != 'i' and go_again != 'n':
                go_again = input("Na ezt most próbáljuk újra. 'i' vagy 'n'?   ").lower()

        if go_again == 'n':
            ongoing = False

game()