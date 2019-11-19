import csv

#file = open("data.csv", "w")
# we use with so we do not need to close the file
with open("data.csv", "w") as file:
    writer = csv.writer(file)  # to create the file
    # to write rows
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1001, 2, 15])

# when open to read a file we do not need to specify the mode
# with open("data.csv") as file:
#     reader = csv.reader(file)  # to create the file
#     # print(list(reader))  # we can put the content inside a list
#     # in this case the previous iteration took the cursor at the end
#     # of the file, therefore the for loop will not print anything
#     # this means that we can iterate with the content of the file once.
#     for row in reader:
#         print(row)

# once we have converted the content of the file in a series of lists
# it will be easy to merge contents from different files
