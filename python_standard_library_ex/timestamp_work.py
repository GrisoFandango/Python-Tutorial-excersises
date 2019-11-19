# give timestamps, datetime instead give date time object like year, month...
import time

# give the current time as timestamp as unix epic time (Second since creation)
print(time.time())
# simulate to send email to kk of users


# def send_email():
#     for i in range(10000000):
#         pass


# this is an example how we can measure how long it takes to execute a code selected
start = time.time()
# send_email()
end = time.time()
duration = end - start
print(duration)
