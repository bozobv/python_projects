from abc import abstractmethod
import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def offer_choose():
    while(True):
        choice = input("Mit kíván a tested, teswérem? (espresso/latte/cappuccino)  ")
        if choice == "report" or choice == "off":
            return choice
        else:
            for name in MENU:
                if name == choice:
                    return choice
        
def print_report():
    for name in resources:
        print(f"{name}: {resources[name]}")
    print(f"Money: ${profit}")
    return
    
def check_ings(product):
    for ingr in MENU[product]["ingredients"]:
        if MENU[product]["ingredients"][ingr] > resources[ingr]:
            print(f"Sorry bro, nincs elég {ingr}")
            return False
    
    return True

def req_money(product):
    
    #ezt be lehet még tenni egy függvénybe
    global profit
    cost = MENU[product]['cost']
    print(f"Ez összesen ${cost} lesz")
    cost -= int(input("Mennyi quarter-t dobsz be?    ")) * 0.25
    cost -= int(input("Mennyi dime-t dobsz be?       ")) * 0.2
    cost -= int(input("Mennyi nickle-t dobsz be?     ")) * 0.05
    cost -= int(input("Mennyi penny-t dobsz be?      ")) * 0.01

    if cost > 0:
        print(f"Ez kevés tesomsz, még {cost} dollár kéne, na próbálkozz újra :) (azt ne kérdezd miért nem dobhatsz be még pár érmét, és helyette előlről kezdheted az egészet...)")
        return False
    elif cost == 0:
        print("pontosan attál tesomsz")
        profit += MENU[product]['cost']
    else: 
        profit += MENU[product]['cost']
        exchange = -round(cost, 2)
        print(f"pöppet túlfizettél testem, itt van vissza ${exchange}")
    time.sleep(1)
    return True

def create_product(product):
    print("Már készül is a kávéd :)")
    time.sleep(2)
    for ingr in MENU[product]["ingredients"]:
         resources[ingr] -= MENU[product]["ingredients"][ingr]
    
    print(f"Parancsolj öcskös, egy {product}")

def coffe_machine():
    
    running = True
    while(running):
        choice = offer_choose()
        if choice == "off":
            return
        if choice == "report":
            print_report()
        else:
            if check_ings(choice):
                if req_money(choice):
                    create_product(choice)
                       
coffe_machine()