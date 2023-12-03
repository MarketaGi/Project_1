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

#username and password for testing purposes
#username = 'bob'
#password = '123'

#testing which part of text to choose
#test = TEXTS[0]
#print(test)
#TEXTS = [1, 2, 3]

#print(len(TEXTS))
if username in registered_users:
    print(line)
    print("Welcome to the app", username,".")
    print("We have", len(TEXTS), "texts to analyze.")
    
else:
    quit("unregistered user, terminating the program..")

print(f"Welcome to the app, {username}. We have {len(TEXTS)} texts to analyzed.")

print(line)
text_number_chosen = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
#text_number_chosen = 1
print(line)
text_index = int(text_number_chosen) - 1   #toto je index, který potrebuju z textu
#print(type(text_index))
#print(text_index)


#test = TEXTS[text_index]    #nevím, co udělat s tímto...
#print(test)

clean_words = []

for word in TEXTS[text_index].split():  #for first text find word and split it
    clean_word = word.strip(",.:;'")
    clean_words.append(clean_word.lower())

#print(clean_words)
#print(len(clean_words)) 

print("There are", len(clean_words), "words in the selected text.")

title_word = 0
for word in TEXTS[text_index].split():
    if word.istitle():
    #for pismeno in word:
        #for pismeno in range(1):
     #   if pismeno.istitle():
        title_word = title_word + 1 
#print(title_word)
#for word in test

print("There are", title_word, "titlecase words.")


uppercase_words  = []  #uppercase words with no digits
uppercase_words_count = 0

for word in TEXTS[text_index].split(): 
    is_numeric = False
    for character in word:
        if character.isdigit():
            is_numeric = True
        #print(character, " ", is_numeric)
    if not is_numeric and word.isupper() :
        uppercase_words.append(word)
        uppercase_words_count = uppercase_words_count + 1 
#print(uppercase_words)
#print(len(uppercase_words))

print("There are", uppercase_words_count, "uppercase words.")



lowercase_words  = []  #uppercase words with no digits
lowercase_words_count = 0

for word in TEXTS[text_index].split(): 
    is_numeric = False
    for character in word:
        if character.isdigit():
            is_numeric = True
        #print(character, " ", is_numeric)
    if not is_numeric and word.islower() :
        lowercase_words.append(word)
        lowercase_words_count = lowercase_words_count + 1 
#print(lowercase_words)
#print(len(lowercase_words))

print("There are", lowercase_words_count, "lowercase words.")


numeric_strings  = []  #uppercase words with no digits
numeric_strings_count = 0


for word in TEXTS[text_index].split(): 
    if  word.isnumeric() :
        numeric_strings.append(int(word))
        numeric_strings_count = numeric_strings_count + 1 
#print(numeric_strings)
#print(len(numeric_strings))

print("There are", numeric_strings_count, "numeric strings.")
#print(numeric_strings)
#print(sum(numeric_strings))

sum_of_all_numbers = sum(numeric_strings)
#print(sum_of_all_numbers)

print("The sum of all the numbers", sum_of_all_numbers,".")
#if text_number_chosen = 1:

#print(clean_words)

occurence = []
for word in clean_words:
    occurence.append(len(word))
#print(max(occurence))


occurences = len("OCURENCES")

print(line)

max_word_length = max(len(word) for word in clean_words)+1
#print(len(str(max_word_length))+1)
number_char_accurence = len(str(max_word_length))+1
#print(max_word_length-occurences)

#print("LEN|  OCCURENCES   |NR.")
#print(f"LEN| OCCURENCES {' ' * ((max_word_length-occurences-1))} |NR.")
word_occurence = {}
for number in range(1,max(occurence)+1): #12 záznamů - max occurence je 11, potřebuji o 1 větší index
    occurence = 0 #count to zero for each lenght
    for word in clean_words:

        if len(word) == number:
            occurence = occurence + 1
    word_occurence[number] = occurence
 #   print(f"{number:3}| {occurence*'*'} {' ' * (max_word_length-occurence)} |{occurence}")
    print(f"{number:{number_char_accurence}}| {occurence*'*'} {' ' * (max_word_length-occurence)} |{occurence}")

