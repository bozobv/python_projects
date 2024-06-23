def asd():
    def basd():
        print("moasd")
    basd()

def format_name(f_name, s_name):
    return(f_name.title() + " " + s_name.title())

def leap_year_calc(year):    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True        
    else:
        return False 

def days_in_month(year, month ):
    """Megmondja mennyi nap van a megadott hónapban a megadott évben"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if (month < 1 | month > 12):
        print("ilyen hónap nincs, :P")
        return -1
    elif (month == 2) and (leap_year_calc(year) == True):
        return month_days[month - 1] + 1
    return month_days[month - 1]
            
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():
      pass    
        
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("Mi az első szám?   "))
num2 = int(input("Mi a máodik szám?  "))

oper = input("Oszt mit csináljunk vele? +, -, * vagy *?  ")
for i in operations:
    if i == oper:
        print(f"{num1} {oper} {num2} = {operations[i](num1, num2)}")