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

clean_words = []  #clean words
title_word = 0    #titlecase words
uppercase_words_count = 0  #uppercase words count
lowercase_words_count = 0
numeric_strings  = []  #uppercase words with no digits
numeric_strings_count = 0

for word in TEXTS[text_index].split():  #for first text find word and split it
    clean_word = word.strip(",.:;'")
    clean_words.append(clean_word.lower())
    if word.istitle():
        title_word += 1 # zkrácený zápis pro přičítání 1 do proměnné

    is_numeric = False
    for character in word:
        if character.isdigit():
            is_numeric = True
    if not is_numeric and word.isupper() :
        uppercase_words_count = uppercase_words_count + 1 
    if not is_numeric and word.islower() :
        lowercase_words_count = lowercase_words_count + 1 
    if  word.isnumeric() :
        numeric_strings.append(int(word))
        numeric_strings_count = numeric_strings_count + 1 

print("There are", len(clean_words), "words in the selected text.")
print("There are", title_word, "titlecase words.")
print("There are", uppercase_words_count, "uppercase words.")
print("There are", lowercase_words_count, "lowercase words.")
print("There are", numeric_strings_count, "numeric strings.")
print("The sum of all the numbers", sum(numeric_strings),".")


occurence = [len(word) for word in clean_words]

#max occurence count for histogram widht
max_occurence_count = max(occurence.count(length) for length in set(occurence))
#print(max_occurence_count)

print(line)

max_word_length = max(len(word) for word in clean_words)+1  #maximální délka slova je 13, ale pythonu potřebuji v indexu přičíst 1

number_char_accurence = len(str(max_word_length))+1

word_occurence = {}

for number in range(1,max(occurence)+1): #12 záznamů - max occurence je 11, potřebuji o 1 větší index
    occurence = 0 #count to zero for each lenght
    for word in clean_words:
        if len(word) == number:
            occurence += 1

    word_occurence[number] = occurence  

    print(f"{number:{number_char_accurence}}| {occurence*'*'} {' ' * (max_occurence_count-occurence)} |{occurence}")



