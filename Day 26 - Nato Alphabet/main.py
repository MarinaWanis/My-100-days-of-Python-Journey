import pandas

user_letter = []
dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in dataframe.iterrows()}

user_input = input("Enter an input: ").upper()

final_dict = [nato_dict[letter] for letter in user_input]

print(final_dict)


