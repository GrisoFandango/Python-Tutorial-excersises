import random
import string

print(random.random())  # create a random number between 0 and 1
print(random.randint(1, 10))  # create random integer between 1 and 10
# choice allow to pick from an array/list/string a number of value equal to the value in k
# we can use as a password generator, the only problem is that the result will be a list
print(random.choices([1, 2, 3, 4], k=2))
print(random.choices("abcdefghilmnopqrst", k=4))
# using joing with a string before it, it will give as result a string and between the values what we punt in ""
print("".join(random.choices("abcdefghilmnopqrst", k=4)))
# to avoid to put all the characters every time we can use the string module
# ascii_letter will give back a string containing all the letters, upper and lower case
print(string.ascii_letters)
# digit do the same with numbers
print(string.digits)
# it is possible to combine the two and use the join as above
print("".join(random.choices(string.ascii_letters+string.digits, k=10)))
# another method to shuffle an array
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
