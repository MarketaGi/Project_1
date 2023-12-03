"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Markéta Giňovská
email: marketa.ginovska@gmail.com
discord: MarketaGi
"""


TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#line to graphically separate the values
line = 50 * "-"

#registered users and passwords
registered_users = ['bob', 'ann', 'mike', 'liz']
user_password = ['123','pass123', 'password123','pass123']

username = input("username: ")
password = input("password: ")

text_lenght = len(TEXTS)

if username in registered_users:
    print(line)
    print("Welcome to the app", username,".")
    print("We have", text_lenght, "texts to analyze.")  
else:
    quit("unregistered user, terminating the program..")

print(f"Welcome to the app, {username}. We have {text_lenght} texts to analyzed.")

print(line)

text_number_chosen = input(f"Enter a number between 1 and {text_lenght} to select: ")

# check if we have number and number between 1-3
while not text_number_chosen.isdigit() or int(text_number_chosen) < 1 or int(text_number_chosen) > text_lenght:
    print(f"You entered an invalid input {text_number_chosen}. Please enter a valid number between 1 and", text_lenght)
    text_number_chosen = input(f"Enter a number between 1 and {text_lenght} to select: ")

#index for chosen text
text_index = int(text_number_chosen) - 1

print(line)

clean_words = [word.strip(",.:;'").lower() for word in TEXTS[text_index].split()]
title_word = sum(1 for word in clean_words if word.istitle())
uppercase_words_count = sum(1 for word in clean_words if word.isupper() and not any(c.isdigit() for c in word))
lowercase_words_count = sum(1 for word in clean_words if word.islower() and not any(c.isdigit() for c in word))
numeric_strings = [int(word) for word in clean_words if word.isnumeric()]
numeric_strings_count = len(numeric_strings)


print("There are", len(clean_words), "words in the selected text.")
print("There are", title_word, "titlecase words.")
print("There are", uppercase_words_count, "uppercase words.")
print("There are", lowercase_words_count, "lowercase words.")
print("There are", numeric_strings_count, "numeric strings.")
print("The sum of all the numbers", sum(numeric_strings),".")


occurence = [len(word) for word in clean_words]

#max occurence count for histogram widht
max_occurence_count = max(occurence.count(length) for length in set(occurence))

print(line)

max_word_length = max(len(word) for word in clean_words)+1  

number_char_accurence = len(str(max_word_length))+1

#word_occurence = {}

#for number in range(1,max(occurence)+1): 
#    occurence = 0 
#    for word in clean_words:
#        if len(word) == number:
#            occurence += 1

#    word_occurence[number] = occurence  

#    print(f"{number:{number_char_accurence}}| {occurence*'*'} {' ' * (max_occurence_count-occurence)} |{occurence}")

word_occurence = {number: sum(1 for word in clean_words if len(word) == number) for number in range(1, max(occurence) + 1)}

for number, occurence in word_occurence.items():
    print(f"{number:{number_char_accurence}}| {occurence*'*'} {' ' * (max_occurence_count-occurence)} |{occurence}")



