import random


def encryption(st, shift):
    res = ""
    space_substitute = ["@", "#", "$", ".", ";", "&", "*", "?", "~", ","]
    for i in st:
        if i == " ":
            res = res + space_substitute[random.randint(0, 9)]
        elif 48 <= ord(i) <= 57:
            res = res + chr((ord(i) + shift - 48) % 10 + 48)
        elif i.isupper():
            res = res + chr((ord(i) + shift - 65) % 26 + 65)
        else:
            res = res + chr((ord(i) + shift - 97) % 26 + 97)
    return res


def decryption(st, shift):
    res = ""
    space_substitute = ["@", "#", "$", ".", ";", "&", "*", "?", "~", ","]
    for i in st:
        if i in space_substitute:
            res = res + " "
        elif 48 <= ord(i) <= 57:
            res = res + chr((ord(i) - shift - 48) % 10 + 48)
        elif i.isupper():
            res = res + chr((ord(i) - shift - 65) % 26 + 65)
        else:
            res = res + chr((ord(i) - shift - 97) % 26 + 97)
    return res


crypt = input("Decrypt or Encrypt (De/En): ")

if crypt == 'En':
    string = input('Enter String: ')
    move = int(input('Enter Shift Key: '))
    encrypted = encryption(string, move)
elif crypt == 'De':
    encrypted = input('Enter your cipher text: ')
    move = int(input('Enter Shift Key: '))

decrypted = decryption(encrypted, move)
print('Original text (input from user): ' + encrypted)
print('Encrypted text: ' + encrypted)
print('Decrypted text (from program): ' + decrypted)