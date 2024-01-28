# Write a Python program to create a file where all letters of the English alphabet are listed by a specified number of letters on each line.

def create_alphabet_file(linesize, filename):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    with open(filename, 'w') as file:
        for i in range(0, len(alphabet), linesize):
            line = alphabet[i:i+linesize]
            file.write(line + '\n')
