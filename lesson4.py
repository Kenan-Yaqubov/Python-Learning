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


# END