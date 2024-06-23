import turtle
import pandas


def check_answer(answer, df):
    return df["state"].str.contains(answer).any()

def add_state(text, df):
    
    lilboy  = turtle.Turtle()
    lilboy.hideturtle()
    lilboy.penup()
    
    lil_posx = int(df[df.state == text].x)
    lil_posy = int(df[df.state == text].y) 
    
    #print(f"{lil_posx} {lil_posy}")
    
    lilboy.goto(lil_posx, lil_posy)
    lilboy.pendown()
    lilboy.write(text, align="center")

screen = turtle.Screen()
screen.title("US namegame")

image = "day25/bigboy/blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

states_df = pandas.read_csv("day25/bigboy/50_states.csv")
all_states = states_df.state.to_list()

correct_guess_counter = 0
guessed_states = []

while 50 > correct_guess_counter:
    
    answer_state = screen.textinput(title=f"Talald ki az állam nevét {correct_guess_counter}/50", 
                                    prompt="Na, öcskös, mondj egy állam nevet az usaban").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
                
        new_df = pandas.DataFrame(missing_states)
        new_df.to_csv("day25/bigboy/states_need_to_learn.csv")
        break
    
    if answer_state not in guessed_states:
        if check_answer(answer_state, states_df):
            add_state(answer_state, states_df)
            correct_guess_counter += 1
            guessed_states.append(answer_state)
            




#beolvasni a fajlt

#csinalni egy teknőckreátort

#ha a guessed rajta van a fájlon, csinálni egy teknőcöt, odatenni a koordinátához

#ha elfogyott, akkor csá




def get_mouse_click_coord(x, y):
    print(x, y)
    
#turtle.onscreenclick(get_mouse_click_coord)

#turtle.mainloop()
    



#screen.exitonclick()