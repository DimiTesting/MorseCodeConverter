# This program will take any string input and convert it to Morse code
import csv

data = {}
with open("morse.csv") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        data.update({row[0]: row[1]})

user_input = input("Hello, please insert a text, we will convert it to Morse code \n")

program_output = ""
for each_letter in user_input:
    matching_format = each_letter.capitalize()
    program_output += data[matching_format]


print(f"Here is your text in Morse code: '{program_output}'")