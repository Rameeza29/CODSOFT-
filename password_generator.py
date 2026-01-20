import random

y= int(input("Enter length num: "))
r = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-={}[]|\":;'<>?,./~`"

lst = []

for i in range(y):
    lst.append(random.choice(r))

print("Password:", "".join(lst))