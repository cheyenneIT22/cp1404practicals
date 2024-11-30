"""CP1404 Practical 03- Program to show different ways to read files."""
from prac_03.capitalist_conrad import out_file

# 1. Asks user for their name, then opens file called "name.txt" and writes to it.
name = input("what is your name?: ")
print(name, file=out_file)
out_file.close()

# 2. Opens "name.txt" and reads the name then prints "Your name is..."
filename = "numbers.txt"
in_file = open("numbers.txt", 'r')
name = in_file.read().strip()
print("your name is", name)
in_file.close()

# 3. Opens "numbers.txt", read the first two nu,bers and adds them together, then prints result.
in_file = open("numbers.txt", 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)
# 4. Prints the total for all lines in "numbers.txt" or a file with any of numbers.
in_file = open("numbers.txt", 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
