import pandas


df = pandas.read_csv("nato_phonetic_alphabet.csv")
my_dict = pandas.DataFrame(df)
phonetic_dictionary = {row.letter: row.code for (index, row) in my_dict.iterrows()}


def generate_word():
    user_input = input("Enter a word ").upper()
    try:
        phonetic_list = [phonetic_dictionary[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alpha please.")
        generate_word()
    else:
        print(phonetic_list)

generate_word()