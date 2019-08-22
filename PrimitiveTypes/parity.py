def parity(x: int) -> int:
    result = 0
    while x:
        print("x is currently: " + str(bin(x)[2:]))
        result ^= 1
        print("result is currently " + str(result))
        a = x & ~(x - 1)
        print ("a is " + str(bin(a)[2:]))
        x &= (x - 1)
    return result

while True:
    try:
        number = int(input("Enter a decimal number: "))
        print("Your number in binary is: " + str(bin(number)[2:]))
        print("The parity of your number is " + str(parity(number)))
        break
    except ValueError:
        print("Invalid input")
