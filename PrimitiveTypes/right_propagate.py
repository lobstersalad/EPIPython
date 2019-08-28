def right_propagate(x: int) -> int:
    return (x | (x - 1))

while True:
    try:
        number = int(input("Enter a decimal number: "))
        print("Your number in binary is: " + str(bin(number)[2:]))
        print("Your number with the rightmost set bit propagated to the right is " + str(bin(right_propagate(number))[2:]))
        break
    except ValueError:
        print("Invalid input")
