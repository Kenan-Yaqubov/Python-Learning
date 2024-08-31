# BEGIN

# str - string :3
# int - number :3
# float - number with point? :3
# abs - makes negative number regular

print(str(2) + " times")
print(int("23"))
print(0.1 + 0.2)
print(float(5))
print(abs(int("-42")))
print(abs(10 + -13))

# ========================================================

# len - founds the length of word
# pow - vozvodit v stepen :3
# round - round's the number

number = 10.1234
motto = 'Family, Duty, Honor'
first_name = '  Grigor   \n '

company1 = "Apple"
company2 = "Samsung"

company1_length = len(company1)
company2_length = len(company2)

print(company1_length + company2_length)
print(pow(company1_length, company2_length))
print(round(15.52, 1))

print(hex(round(number)))
print(type(motto))

print(first_name.strip())

# END