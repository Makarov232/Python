from module import *

load_words()
word_description = get_random_word_and_desc()
word = word_description[0].lower()
description = word_description[1]

lives = get_lives()
symbol = get_symbol()
displayed = make_word_displayed(symbol, len(word))
f_val = True

while is_alive(lives) and symbol in displayed:
    print("\nОбъяснение:", description)
    show_hangman(lives)
    display_word(displayed)
    answer = get_user_answer("\nВведите букву или всё слово: ")

    if answer == word:
        f_val = False
        break
    if len(answer) == 1 and check_letter_in_word(answer, word):
        displayed = replace_letters_in_displayed(answer, displayed, word)
    else:
        lives = take_life_away(lives)

if f_val:
    show_hangman(lives)
    display_word(displayed)
    check_win_or_lose(word, displayed)
else:
    print("\nВы выиграли, УРААА!!!")
