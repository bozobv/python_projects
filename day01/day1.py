def bmi_calc():
    print("BMI calculátor")

    h = float(input("mondj egy magasságot méterben   "))
    w = int(input("mondj egy súlyt   "))

    bmi = w / (h ** 2)

    if (bmi > 35):
        print(f"A bmi-d {bmi}, és tesó, klinikailag túlsúlyos vagy!")
    elif (bmi > 30):
        print(f"A bmi-d {bmi}, és tesó, túlsúlyos vagy!")
    elif (bmi > 25):
        print(f"A bmi-d {bmi}, és tesó, pöppet túlsúlyos vagy!")
    elif (bmi > 18.5):
        print(f"A bmi-d {bmi}, és tesó, normál vagy!")
    else:
        print(f"A bmi-d {bmi}, és tesó, alultáplált vagy!")
        
        
#ha néggyel osztható, szököév, de ha 100-zal osztható, nem az, kivéve ha 400-zal osztható        
def leap_year_calc():
    year = int(input("mondj egy évet  "))
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("szökőév tesó")
            else:
                print("hát tesomsz, majdnem, de ez nem szökőév")
        else:
            print("szökőév, tesó!")        
    else:
        print("hát tesomsz, ez nem szökőév")   
        
def leap_year_calc2():
    year = int(input("mondj egy évet  "))
    
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        print("szökőév, tesó!")
    else:
        print("hát tesomsz, ez nem szökőév")    
        
def pizza_order():
    
    size = input("mekkora pizza legyen, S, M vagy L   ")
    pep = input("pepperoni? Y or N   ") 
    cheese = input("cheese? Y or N   ")
    
    if (size == 'S'):
        bill = 15
        
    elif(size == 'M'):
        bill = 20
        
    elif (size == 'L'):
        bill = 25 
    
    if pep == 'Y':
        if size == 'S':
            bill += 2 
        else:
            bill += 3
    
    if (cheese == 'Y'):
        bill += 1
        
    print(f"az ára {bill}")
    
        
    
  
        
