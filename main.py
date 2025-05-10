"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lucie Mazánková
email: mazankovalu@gmail.com
"""

# registrovaní uživatelé a jejich hesla
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
} 

# nabízené texty
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
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

# vstup od uživatele - jméno a heslo
username = input("Please enter your username:")
password = input("Please enter your password:")

print("----------------------------------------")

# ověření uživatele a správnosti hesla
if username in users and users [username] == password:
    print(f"Welcome to the app, {username}!\nWe have {len(TEXTS)} texts to by analyzed.")
    print("----------------------------------------")
else:
    print("Unregistered user, terminating the program.")
    exit()

# výběr textu
print("Enter the number of the text you selected:")
choice = input("The text number:")
print("----------------------------------------")

# ověření, že bylo na vstupu zadáno správné číslo
if not choice.isdigit() or not 1 <= int(choice) <= len(TEXTS):
    print("You did not enter a correct number, terminating the program.")
    exit()

# vybraný text
text = TEXTS [int(choice) - 1]

# rozdělení textu na jednotlivá slova
words = text.split()

# hodnoty proměnných
total_words = 0
titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
numeric_words = 0
sum_of_numbers = 0

# slovník pro počítání délek slov
word_lengths = {}

# procázení slov a odstranění interpunkce
for word in words:
    clean_word = word.strip("-:.,!?")
    if clean_word == "":
        continue

    total_words += 1

    if clean_word.istitle():
        titlecase_words += 1
    elif clean_word.isupper():
        uppercase_words += 1
    elif clean_word.islower():
        lowercase_words += 1

    if clean_word.isnumeric():
        numeric_words += 1
        sum_of_numbers += int(clean_word)

    length = len(clean_word)
    if length in word_lengths:
        word_lengths[length] +=1
    else:
        word_lengths[length] = 1

# výsledky
print(f"There are {total_words} words in the selected text.")
print(f"There are {titlecase_words} titlecase words.")
print(f"There are {uppercase_words} uppercase words.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There are {numeric_words} numeric strings.")
print(f"The sum of all the numbers {sum_of_numbers} .")
print("----------------------------------------")
print("LEN|      OCCURENCES      |NR.")
print("----------------------------------------")

# graf
for length in sorted(word_lengths):
    stars = "*" * word_lengths[length]
    print(f"{length:>3}| {stars:<20} |{word_lengths[length]}")

print("----------------------------------------")
print(f"That's all from the text analysis, {username}. Have a nice day!")