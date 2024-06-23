import art
import random
 
HARDNESS = {
    "baby" : 10,
    "mid" : 7,
    "man" : 5,
}

def choose_difficulity():
    while True:
        diffic = input("Írd hogy 'baby', ha az első, 'man' ha az utóbbi, vagy 'mid', ha közepes szint   ")
        if diffic in HARDNESS:
            return HARDNESS[diffic]  
        
def compare(player_guess, secret_number):
    if player_guess > secret_number:
        print("nem jó, túl NAGY (úristen, very big)")
        return False
    elif player_guess < secret_number:
        print("nem jó, túl KICSI (nem a méret a lényeg amúgy)") 
        return False
    else:
        print("NAGYON JÓ VAGY, PONT JÓ!!!")    
        return True  

def game_cycle(secret_number, trys_left):
    while True:
        print(f"\n{trys_left} próbálkozásod van még hátra")
        player_guess = int(input("Mondj egy számot:  "))
        won = compare(player_guess, secret_number)
        if won == True:
            print("Emberiséghez méltó győzelem a mesterséges intelligencia felett!!! Hurrá!!")
            return
        trys_left -= 1
        if trys_left < 1:
            print("Szégyenteljes vereség, kis barátom")
            return 
    
def ask_again():
    while True:
        more = input("szeretnél még egy kört veretni? igen/nem    ").lower()
        if more == "igen":
            return True
        elif more == "nem":
            return False
        print("Látom nem sikerült, na még egyszer")

def game():

    art.guess_number_logo()
    again = True
    
    while(again):
        print("""talald ki a számot, pupák
gondoltam egy számra 1 és 100 közöt
milyen nehézségi szintet választasz, dedós vagy férfias? 
""")
        trys_left = choose_difficulity()
        secret_number = random.randint(1, 100)
        
        game_cycle(secret_number, trys_left)
        
        again = ask_again()
        
        
game()
        
            
    
    
    
    
    
    