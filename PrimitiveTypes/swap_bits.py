def swap_bits(x:int, i: int, j: int) -> int:
    if ((x >> i & 1) != (x >> j & 1)):
        # print("Bits are different")
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x

while True:
    try:
        number = int(input("Enter a decimal number: "))
        print(number.bit_length())
        i = int(input("Enter i: "))
        if (i > number.bit_length() - 1 or i < 0):
            raise ValueError("i is out of bounds")
        j = int(input("Enter j: "))
        if (j > number.bit_length() - 1 or j < 0):
            raise ValueError("j is out of bounds")
        print("Your number in binary is: " + str(bin(number)[2:]))
        number = swap_bits(number, i, j)
        print("Your number with bits " + str(i) + " and " + str(j) + " swapped is: " + str(bin(number)[2:]) + " or " + str(number))
        break
    except ValueError as error:
        print(error)
