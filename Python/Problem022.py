"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 +15 +12 +9 +14 =53, is the 938th name in the list. So, COLIN would
obtain a score of 938 x 53 =49714.

What is the total of all the name scores in the file?

871198282

What did I learn doing this?
- Reading files, remembered how to use that.
- Used a dictionary in a pretty smart way.
- Used enumerate well!
"""

LETTER_VALS = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}

def name_value(name:str):
    name_val = 0
    for letter in name:
        # print(f"Letter {letter} value {LETTER_VALS[letter]}")
        name_val += LETTER_VALS[letter]
    return name_val

def main():
    file_name = "names.txt"
    with open(file_name, 'r') as file:
        name_list = file.read()
    names = name_list.split(",")
    stripped_names = set()
    for name in names:
        stripped_name = name.strip('\"')
        stripped_names.add(stripped_name)
    names = sorted(stripped_names)
    total_name_values = 0
    for index, name in enumerate(names, 1):
        # print(f"Name {name} is index {index}")
        name_val = index * name_value(name)
        total_name_values += name_val
        if name == "COLIN":
            print(f"Name {name} is index {index}. Value {name_val}")
    print(f"Names total {total_name_values}")



if __name__ == '__main__':
    main()
