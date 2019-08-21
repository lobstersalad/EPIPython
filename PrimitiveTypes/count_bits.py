def count_bits(x: int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

while True:
    try:
        number = int(input("Enter a decimal number: "))
        print("Your number in binary is: " + str(bin(number)[2:]))
        print("There are " + str(count_bits(number)) + " bits in your number!")
        break
    except ValueError:
        print("Invalid input")
