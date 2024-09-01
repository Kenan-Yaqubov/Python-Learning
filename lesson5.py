# BEGIN

# < — меньше
# <= — меньше или равно
# > — больше
# >= — больше или равно
# == — равно
# != — не равно

def has_upper_case(text: str) -> str:
    return text != text.lower()


print(has_upper_case('it woRks'))
print(has_upper_case('it works'))


# =========================================================

#       И and
# A	    B	    A and B
# True	True	True
# True	False	False
# False	True	False
# False	False	False

#       ИЛИ or
# A	    B	    A or B
# True	True	True
# True	False	True
# False	True	True
# False	False	False

def is_leap_year(year: int) -> int:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


print(is_leap_year(2016))
print(is_leap_year(2019))


# Число 0 эквивалентно False
# Значение False уже является False
# Пустая строка ('') эквивалентна False
# Пустой список [] эквивалентен False
# Число 42 эквивалентно True
# Строка "Hello" также эквивалентна True

def string_or_not(text):
    return isinstance(text, str) and 'yes' or 'no'


print(string_or_not('5'))
print(string_or_not(5))


# =========================================================

def normalize_url(url):
    https = 'https://'
    if url[:8] == https:
        return url
    elif url[:7] == 'http://':
        return url.replace('http://', https, 1)
    else:
        return https + url


print(normalize_url("http://kenan"))


def get_number_explanation(num: int) -> int:
    match num:
        case 666:
            return 'devil number'
        case 42:
            return 'answer for everything'
        case 7:
            return 'prime number'
        case _:
            return "just a number"


print(get_number_explanation(42))

# =========================================================


def print_numbers(num: int):
    while num > 0:
        print(num)
        num -= 1
    print('finished!')


print_numbers(5)
# END
