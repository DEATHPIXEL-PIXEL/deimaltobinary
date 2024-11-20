decimal_number = int(input("Enter a decimal number: "))

binary_number = ""
while decimal_number > 0:
    binary_number = str(decimal_number % 2) + binary_number
    decimal_number //= 2

print("Binary representation:", binary_number)