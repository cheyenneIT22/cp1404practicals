"""Files."""
out_file = open("name.txt", 'w')
name = input("what is your name?: ")
print(name, file=out_file)
out_file.close()

filename = "numbers.txt"
in_file = open("numbers.txt",'r')
name = in_file.read().strip()
in_file.close()
print("your name is",name)

in_file = open("numbers.txt", 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

in_file = open("numbers.txt", 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)