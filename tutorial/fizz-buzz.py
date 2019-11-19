def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "fizzbuzz"
    elif input % 3 == 0:
        return "fizz"
    elif input % 5 == 0:
        return "buzz"
    return input


print(fizz_buzz(15))
print(fizz_buzz(5))
print(fizz_buzz(3))
print(fizz_buzz(7))

sentence = "This is a common interview question"
print(sentence)
for x in sentence:
    print = x
