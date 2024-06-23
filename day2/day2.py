import random


def print_coin(coin):
    if (coin == 0):
        print("Fejet dobtunk")
    elif(coin == 1):
        print("Írást dobtunk ")
        
def coin_compare(coin, tipp):
    if((coin == 0 and tipp == "Fej") or (coin == 1 and tipp == "Írás")):
            print("eltaláltad")
    else:
        print("béna vagy, nem találtad el") 

def coin_flip():
    continuing = True
    while(continuing):
        tipp = input("Fej vagy Írás? (nagybetűvel az elsőt)  ")
        coin = random.randint(0,1)
        
        print_coin(coin)
            
        coin_compare(coin, tipp)
            
        if (input("akarsz újra próbálkozni? Igen vagy Nem? ") != "Igen"):
            continuing = False
    
def bill_roulette(names):
    print("ki fog fizetni? ")
    print(names[random.randint(0, len(names) - 1) ])

def hide_treasure():
    map = [
        ["0","0","0"],
        ["0","0","0"],
        ["0","0","0"] 
    ]
    
    hiding_place = input('''Egy kitoszott kalóz vagy. Az alábbi térképen hova durrantanád be a kincset?
    A1, A2, A3
    B1, B2, B3
    C1, C2, C3
    ''' )
    
    if len(hiding_place) != 2:
        print("Hibás input! Kérem, adjon meg egy kétbetűs stringet.")
    else:
        row = ord(hiding_place[0].upper()) - ord('A')  # Számított sor index
        col = int(hiding_place[1]) - 1  # Számított oszlop index
        
        if 0 <= row < len(map) and 0 <= col < len(map[0]):
            # Kiírjuk az eredményt
            map[row][col] = "X"
            print(f" Itt a kincsedm kutyan \n{map[0]}\n{map[1]}\n{map[2]}\n")
        else:
            print("Hibás input! A megadott hely nincs a térképen.")
    
def rock_print():
    # Rock
    print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """)

def scissor_print():
    # Scissors
    print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)
    
def paper_print():
    # Paper
    print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """)

def handprint(hand):
    if(hand == "kő"):
        rock_print()
    elif hand == "olló":
        scissor_print()
    elif hand == "papír":
        paper_print()
    
def battle(hand1, hand2):
    if (hand1 == hand2):
        print("döntetlen")
    elif((hand1 == "papír" and hand2 == "kő") or \
         (hand1 == "kő" and hand2 == "olló") or \
         (hand1 == "olló" and hand2 == "papír")):
        print("brutális győzelem a mesterséges intelligencia felett!!!!!!!")
    else:
        print("szégyenteljes vereség a mesterséges intelligencia ellen")    

def rock_paper_scissor():
    hands = ["kő", "papír", "olló"]
    
    player_hand = input("kő, papír, olló  ")
    handprint(player_hand)
    
    computer_hand = hands[random.randint(0,2)]
    handprint(computer_hand)
    
    battle(player_hand, computer_hand)
    
    
rock_paper_scissor()
    
    
    
    
    
    
    
