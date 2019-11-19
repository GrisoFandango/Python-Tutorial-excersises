try:
    age = int(input("Insert your age: "))
    xfactor = 10 / age
except ValueError:
    print("Sorry you did not enter a valid age")
except ZeroDivisionError:
    print("Age cannot be age")
else:
    print("No Exemption were thrown")
