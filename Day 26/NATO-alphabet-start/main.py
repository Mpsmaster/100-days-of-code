import pandas

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
    print(row.student)
    
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# valid_word = True
# while valid_word:
#     try:
#         user_input = input("Enter a word: ").upper()
#         phonetic_list = [nato_dict[letter] for letter in user_input]
#         print(phonetic_list)
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#     else:
#         valid_word = False
#         print("Thank you for using the phonetic code generator.")
def generate_phonetic():
    try:        
        user_input = input("Enter a word: ").upper()
        phonetic_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
            print("Sorry, only letters in the alphabet please.")
            generate_phonetic()
    else:        
        print(phonetic_list)

generate_phonetic()