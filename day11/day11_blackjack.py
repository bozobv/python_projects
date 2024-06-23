import random
import time

cards = [
    ('Ace', 11), 
    ('King', 10), 
    ('Queen', 10), 
    ('Jack', 10),
    ('10', 10), 
    ('9', 9), 
    ('8', 8), 
    ('7', 7), 
    ('6', 6), 
    ('5', 5),
    ('4', 4), 
    ('3', 3), 
    ('2', 2)
]

def print_welcome():
    print("""
üdv, Faszos, a python blackjacken!
a szabályokat nem fogom elmondani, mert lusta vagyok leírni, keress rá.
sok sikert!
          """)

def create_deck():

    deck_num = 0
    while(deck_num < 1):
        deck_num = int(input("hány kártyapakliból keverjük ki a játékpaklit (0-nál többet adj)?   "))

    deck = cards * deck_num * 4
    
    return deck

def add_card(deck, hand):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)

def get_starter_hand(deck):
    hand = []

    for i in range(2):
        add_card(deck, hand)
        
    return hand      

def get_hand_value(hand):
    
    value = 0
    aces_num = 0
    
    for card in hand:
        value += card[1]
        if card[0] == 'Ace':
            aces_num += 1

    while value > 21 and aces_num:
        value -= 10
        aces_num -= 1

    return value

def print_player_hand(player_hand):
    print(f"\nez van a kezedben, öcskös:  {player_hand}")
    print(f"\nennyi az értéke:   {get_hand_value(player_hand)} \n")  

def player_turn(player_hand, deck):
    
    if get_hand_value == 21:
        return "win"
    
    decision = input("""
na mit mondasz pupák, húzol még, 
vagy jó lesz ez így? ha húzol, írj egy i-t, 
ha nem akarsz húzni és az osztó jön, nyomj egy n-t  
                     """).lower()
    
    while (decision != 'i' and decision != 'n'):
        decision = input("hülyeséget írsz. i vagy n????").lower()
    
    while (decision == 'i'):

        print("húzol egy lapot")
        add_card(deck=deck, hand=player_hand)

        print_player_hand(player_hand)

        value = get_hand_value(player_hand)
        if value == 21:
            print("nyertéééél, yeees")
            return "win"
        elif (value > 21):
            print(f"vesztettél, béna vagy")
            return "lose"
        
        decision = input("még tovább? n vagy i? ").lower()

    return "stand"

def dealer_turn(dealer_hand, deck, player_hand):

    dealer_value = get_hand_value(dealer_hand)

    if dealer_value == 21:
        print("ez egy messzemenőkig szánalmas vereség!")
        return

    player_value = get_hand_value(player_hand)
    print_full_dealer_hand(dealer_hand)

    while (dealer_value < player_value):
        time.sleep(2)
        add_card(hand=dealer_hand, deck=deck)
        dealer_value = get_hand_value(dealer_hand)

        print_full_dealer_hand(dealer_hand)

        if dealer_value > 21:
            print("NYERTÉL TESWÉREM! DICSŐSÉG A NEMZETÜNKRE")
            return
        
    print("szégyenteljes vereség, jóbarátom")
    return

def print_dealer_hand(hand):
    print(f"\nez látod a gonosz osztó előtt:  {hand[0]}")
    #print(f"ennyi az értéke:   {get_hand_value(hand)}")  

def print_full_dealer_hand(hand):
    print(f"ez látod a gonosz osztó előtt:  {hand}")
    print(f"ennyi az értéke:   {get_hand_value(hand)}")  

def play(player_hand, dealer_hand, deck):

    print_dealer_hand(dealer_hand)
    print_player_hand(player_hand)

    player_turn_end = player_turn(player_hand, deck)

    if player_turn_end == "stand":
        dealer_turn(dealer_hand, deck, player_hand)

def get_continue_intention():
    while(True):
        decision_input = input("""na jó, ezután akarod folytatni? írd hogy i, ha igen, n, ha nem   """).lower()

        if decision_input == 'i':
            return True
        if decision_input == 'n':
            return False
        print("tesomsz, próbáljuk újra")

def game():

    print_welcome()

    decision = True

    while(decision == True):
        deck = create_deck()

        player_hand = get_starter_hand(deck)
        dealer_hand = get_starter_hand(deck)

        play(player_hand, dealer_hand, deck)

        decision = get_continue_intention()
        
game()