"""Loops that display all odd numbers between 1 and 20"""
# displays all odd numbers between 1 and 20 with spaces.
for i in range(1, 21, 2):
    print(i, end="")
print()
# counts numbers in 10s from 0 to 100.
for i in range(0, 101, 10):
    print(i, end="")
print()
# count down from 20 to 1.
for i in range(0, 20, -1):
    print(i, end="")
print()
# prints number of stars in one line.
number = int(input("Number of Stars: "))
print('*' * number)
