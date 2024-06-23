#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


#read all names

def create_invitations(invitation_file, name_file):

    with open(invitation_file, "r") as file:
        inv_content = file.read()
    
    with open(name_file, "r") as names_file:
        names = names_file.readlines()

    names = [name.strip() for name in names]

    for name in names:
        friend_invitation = inv_content.replace("[name]", name)
        with open(f"day24/file/Mail Merge Project Start/Output/ReadyToSend/invitation_{name}.txt", "w") as friend_file:
            friend_file.write(friend_invitation)


#name_list = []
#
#for line in lines:
#    name_list.append(line)
#
#letter_skeleton = "asd"
#
#with open("day24/file/Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
#    lines = file.readlines()
#
#print(lines)
    
create_invitations("day24/file/Mail Merge Project Start/Input/Letters/starting_letter.txt", 
                   "day24/file/Mail Merge Project Start/Input/Names/invited_names.txt")




