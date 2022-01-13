import pandas

# Creates Dataframe from csv file of phonetic alphabet
df = pandas.read_csv('nato_phonetic_alphabet.csv')
# Creates dictionary using list comprehension of Dataframe
keys = {row.letter: row.code for (index, row) in df.iterrows()}

# Defines function to transform word to phonetic spelling
def natofy():
    word = input("What word do you wanna spell?: ")
    try:
        letter_list = [keys[key] for key in word.upper()]
    except KeyError:
        print('Sorry, only letters in the alphabet please!')
        natofy()
    else:
        print(letter_list)

# Calls function
natofy()
