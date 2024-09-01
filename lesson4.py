# BEGIN

# Corrected version

def print_motto():
    print('Winter is coming')


print_motto()


def say_hurray_three_times():
    word = 'hurray!'
    text = f'{word} {word} {word}'
    return text


result = say_hurray_three_times()
print(result)

# =========================================================================


def truncate(text, length):
    newText = f'{text[0:length]}...'
    return newText


print(truncate('Lets goo', 6))


def get_hidden_card(card_numbers, hidden_nums=4):
    strCardNums = str(card_numbers)
    hidden_card_number = f'{'*' * hidden_nums}{strCardNums[-5:-1]}'
    print(hidden_card_number)


get_hidden_card(1234123412341234, 3)
get_hidden_card(1234123412341545)


def trim_and_repeat(text, offset=0, repetitions=1):
    new_text = text[offset:len(text)] * repetitions
    return new_text


trim_and_repeat('asdasd', 5, 2)


def letter_multiply(text: str, letter: str, count: int) -> str:
    new_text = text.replace(letter, letter*count)
    return new_text


print(letter_multiply('python', 'n', 4))


def get_age_difference(lil: int, big: int) -> int:
    return f'The age difference is {abs(big - lil)}'


print(get_age_difference(2011, 2014))
# END