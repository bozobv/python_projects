import os



def student_results():

    student_scores = {
        "satya" : 55,
        "petyka" : 69,
        "luca" : 44,
        "Mária" : 99,
        "Ádám" : 42
    }

    student_grades = {}

    for name in student_scores:

        score = student_scores[name]

        if score > 90:
            student_grades[name] = "Példás"
        elif score > 80:
            student_grades[name] = "Jó"
        elif score > 70:
            student_grades[name] = "Elégséges"
        else:
            student_grades[name] = "Hugyos"



    print(student_grades)

travel_log = [
        {"country" :"France", 
         "cities visited" : ["Paris", "Lille", "Lyon"], 
         "total visits" : 12},
        {"country" :"Germany" , 
         "cities visited" : ["Berlin", "München", "Bremen"], 
          "total visits" : 2} 
    ]


def add_new_country(country, visit_number, cities):

    new_item_num = len(travel_log)

    new_item = {"country" : country, +
         "cities visited" : cities, 
         "total visits" : visit_number}

    travel_log.append(new_item)
    
    return

def traveling():
    travel_log = [
        {"country" :"France", 
         "cities visited" : ["Paris", "Lille", "Lyon"], 
         "total visits" : 12},
        {"country" :"Germany" , 
         "cities visited" : ["Berlin", "München", "Bremen"], 
          "total visits" : 2} 
    ]

    print(travel_log["France"]["cities visited"])

def blind_bidding():

    bidders = {}

    stopped = False
    name = ""


    while (stopped == False):


        name = input("Mi a neved   ")
        bidders[name] = int(input("Mennyi lóvét teszel fel?  $"))

        cont = input("Van még aki fogadni akar? igen/nem  ").lower()

        if cont == "nem":
            print("jóvan, akkor megállunk")
            stopped = True
        elif cont != "igen":
            print("tanulj meg irni")

    max = 0
    winner = "senki sem tett semmit, faszák vagytok"
    for name in bidders:
        if bidders[name] > max:
            max = bidders[name]
            winner = name

    print(f"A győztes, a hatalmas {winner}!!!!!! Ilyen sok pénzt vesztett: ${max}")


blind_bidding()



