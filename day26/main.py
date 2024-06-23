
import random

def task1():
    numbers = [1, 2, 3]

    new_numbers = [n + 1 for n in numbers]

    print(new_numbers)

def task2():
    name = "Alfonz"

    my_list = [letter for letter in name]   
    print(my_list)

def task3():
    
    my_list = [i * 2 for i in range(1, 5)]

    
    print(my_list)

def task4():

    names = ["anyád", "kolbászfa", "jurtafarkú malac", "fos", "répa", "retek", "alex hormozi", "bözses"]

    my_list = [name.upper() for name in names if len(name) > 5]

    print(my_list)

def task5():
    nums = [ 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    sq_nums = [number**2 for number in nums]

    print(sq_nums)

def task6():
    list_of_strings = input().split(',')

    nums = [int(n) for n in list_of_strings]

    even_nums = [n for n in nums if n%2 == 0]

    print(even_nums)

def task7():

    with open("day26/file1.txt") as file1:
        list1 = file1.readlines()

    with open("day26/file2.txt") as file2:
        list2 = file2.readlines()


    list3 = [int(num) for num in list1 if num in list2]

    print(list3)
    
def task8():
    #missings = [ state for state in all_states if state not in guessed_states ]
    pass

def task9():
    names = ["anyád", "kolbászfa", "jurtafarkú malac", "fos", "répa", "retek", "alex hormozi", "bözses"]

    student_scores = { student:random.randint(1,100) for student in names}

    passed_bois = { student:point for (student,point) in student_scores.items() if point > 40}

    print(student_scores)
    print(passed_bois )
     

def task10():

    sentence = input().split(' ')

    sen_dic = {word:len(word) for word in sentence}

    print(sen_dic)

def task11():
    weather_c = eval(input())

    weather_f = {day: num* 9/5 + 32 for (day,num) in weather_c.items()}

    print(weather_f)

