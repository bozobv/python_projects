import turtle
from prettytable import PrettyTable


def turtle_test():
    my_screen = turtle.Screen()
    my_screen.bgcolor("black")
    
    satya = turtle.Turtle()
    satya.shape("turtle")
    satya.color("coral", "green")
    
    print(my_screen.canvheight)
    
    satya.forward(100)
    
    my_screen.exitonclick()

def table_maker():
    table = PrettyTable()
    table.add_column("pokémon", ["Csicskachu", "Sexmander", "Bulbaszar"])
    table.add_column("típus", ["elektronyos", "tüzes", "füves"])
    table.align["típus"] = "l"

    print(table)

    


table_maker()