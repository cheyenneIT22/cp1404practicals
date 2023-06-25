"""Lists exercises"""
# 1.
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(numbers)
    print("The first number is ", numbers[0])
    print("The second number is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("the largest number is", max(numbers))
    print("The average of all the numbers is", sum(numbers) / len(numbers))

# 2.
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter a username:  ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
