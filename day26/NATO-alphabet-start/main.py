import pandas

def before():

    student_dict = {
        "student": ["Angela", "James", "Lily"], 
        "score": [56, 76, 98]
    }

    #Looping through dictionaries:
    for (key, value) in student_dict.items():
        #Access key and value
        pass

    student_data_frame = pandas.DataFrame(student_dict)

    #Loop through rows of a data frame
    for (index, row) in student_data_frame.iterrows():
        #Access index and row
        #Access row.student or row.score
        pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
    
nato_df = pandas.read_csv("day26/NATO-alphabet-start/nato_phonetic_alphabet.csv")

alphabet = {row.letter:row.code for (index, row) in nato_df.iterrows() }


succ = True

while(succ):
    my_word = input()
    try:
        magic_words = [alphabet[letter.upper()] for letter in my_word]
    except KeyError:
        print("tesomsz, ez csak BETŰkből állhat, te meg nem azokat irsz. Próbáld újra!!!!s")
    else:
        succ = False


print(magic_words)


