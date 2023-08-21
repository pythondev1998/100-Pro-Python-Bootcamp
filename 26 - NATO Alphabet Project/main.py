import pandas


data = pandas.read_csv("./nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

your_name = input("Enter a word:").upper()
output_list = [phonetic_dict[letter] for letter in your_name]

print(output_list)