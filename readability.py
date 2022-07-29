# readability of texts
from cs50 import get_string

# declaration of variables
tally_letters = tally_words = tally_sentences = tally_letters = tally_sentences = 0
tally_words = 1

# request texts from user
s = get_string("Texts: ")

for i in s:
    if i.isalpha() == True:
        tally_letters += 1
    if i == " ":
        tally_words += 1
    if i == '.' or i == '?' or i == '!':
        tally_sentences += 1

# calculate the averages
L = tally_letters / (tally_words * 0.01)
S = tally_sentences / (tally_words * 0.01)

# apply the coleman-Liau Index
index = round(0.0588 * L - 0.296 * S - 15.8)

# print grades
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
