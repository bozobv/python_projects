
def error_test():
    try:
        file = open("day30/kolbasz.txt")
    except FileNotFoundError:
        print("Brutális hiba")
        file = open("kolbasz.txt", "w")
        file.write("kolbasz")
    except KeyError as error_massage:
        print(f"a {error_massage}-nek nincs kulcsod")    
    else:
        content = file.read()
        print(content)
    finally:
        file.close()
        print("becsukva a fájl")
        raise TypeError("Kamuhiba, amugy sikerült :P")
    
def error_test2():
    height = float(input("Height:  "))
    if height > 3:
        raise TypeError("bruh ")

def make_pie(fruits, index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print("fruit pie") 

def pie_index_test():
    fruits = eval(input("gyümik: "))
    
    make_pie(fruits=fruits, index=6)

pie_index_test()