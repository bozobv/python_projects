
import csv
import pandas


def basic_csv_reading():
    with open("day25/weather_data.csv", "r") as file:
        content = csv.reader(file)
        print(content)
        
        temperatures = []
        
        for row in content:
            if row[1] != 1:
                temperatures.append(row[1])
            
        print(temperatures)
        
        
def exercise():
    data = pandas.read_csv("day25/weather_data.csv")
    #temp_list = data["temp"]
    #print(data["temp"].max())
    #print(data.day)
    #legmagasabb hőm napja
    #print(data[data.temp == data.temp.max()].temp * 9/5 + 32 )

    data_dict = {
        "kolbasz" : ["gyulai", "szegedi", "házi"],
        "súly" : [69, 96, 1000]
    }

    data = pandas.DataFrame(data_dict)
    data.to_csv("day25/kolbaszok.csv")


#hány darab mókus van a kkülönböző zinekbvől, Primary Fur Color

#colors = {"gray" : 0, "cinnamon" : 0, "black" : 0}

df = pandas.read_csv("day25/2018_squirrel_data.csv", usecols=["Primary Fur Color"])
color_count = df["Primary Fur Color"].value_counts()           
color_count.to_csv("day25/squirrels_by_color.csv")

