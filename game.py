import os

word_secret = "password"
letters_ok = ""

flag = True

qtd_tries = 0

while True:

    print("===== Starting Game =====")

    while flag:

        qtd_tries += 1

        letter_type = input("Type only a letter: ")

        if len(letter_type) > 1:
            print("Error. Type only one letter. Try again: ")
            continue

        if letter_type in word_secret:
            letters_ok += letter_type

        word_form = ''

        for letter in word_secret:
            if letter in letters_ok:
                word_form += letter
            else:
                word_form += '*'

        print(word_form)

        if word_form == word_secret:
            os.system('clear')
            print("Success! You win!")
            print("Tries: ", qtd_tries)
            letters_ok = ""
            qtd_tries = 0
            flag = None

    status_process = input(
        "Do you wanna play again? [s/n]: ".lower())

    if status_process == 's':
        flag = True
    elif status_process == 'n':
        print("===== End Game =====")
        break
    else:
        print(
            "Error. You can't type more than one caractere, only: s or n. Try again.")
        continue
