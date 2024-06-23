import random

def avg_heights():
    student_heights = input().split()
    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])


    counter = 0
    sum = 0

    for height in student_heights:
        sum += height
        counter += 1

    print(f"ennyien vannak: {counter} \nennyi a magasságok összege {sum} \nennyi az átlag: {sum/counter}")

def highest_value():
    student_scores = input("adj egy csomoó számot   ").split()

    if len(student_scores) <= 0:
        print("literálisan nem irtál semmit, tesomsz")
        return

    for n in range(0,len(student_scores)):
        student_scores[n] = int(student_scores[n])

    highest = student_scores[0]

    for score in student_scores:
        if highest < score:
            highest = score
    
    print(f"a legmagasabb szám ezek közül a {highest}")

def even_sum():
    target = int(input("adj egy számot 0 és 1000 között, ahol megszámoljuk a páros számok összegét  "))
    if (target > 1000 or target < 0):
        print("teso, ez neked nagyon nem megy")    
        return
    
    sum = 0
    for n in range(0, target + 1, 2):
        sum += n

    print(sum)

def fizzbuzz():

    for n in range(1, 101):
        out = ""
        if n % 3 == 0:
            out += "Fizz"
        if n % 5 == 0:
            out += "Buzz"
        
        if out == "":
            print(n)
        else:
            print(out)

def password_generator():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
               'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    pw_len = nr_letters + nr_numbers + nr_symbols
    pw = ""

    password_list = []

    
    password_list = [random.choice(letters) for i in range(nr_letters)]
    password_list += [random.choice(symbols) for i in range(nr_symbols)]
    password_list += [random.choice(numbers) for i in range(nr_numbers)]


    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char


#    for i in range(pw_len, 0, -1):
#        choice = random.uniform(0,1)
#        if choice < (nr_letters / i):
#            nr_letters -= 1
#            pw += random.choice(letters)
#        elif choice < ((nr_letters + nr_numbers) / i):
#            nr_numbers -= 1
#            pw += random.choice(numbers)
#        else:
#            pw += random.choice(symbols)
#
    print(f"A szuperduper titkos jelszód ez:  {password}")




password_generator()
