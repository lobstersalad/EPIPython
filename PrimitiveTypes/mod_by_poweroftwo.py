def mod_by_poweroftwo(x: int, y: int) -> int:
    return (x & y - 1)

while True:
    try:
        number = int(input("Enter a decimal number: "))
        mod_by = int(input("Enter a power of two: "))
        if (mod_by > 0) and (mod_by & mod_by - 1 == 0):
            print(str(number) + " mod " + str(mod_by) + " = " + str(mod_by_poweroftwo(number, mod_by)))
        else:
            raise ValueError
        break
    except ValueError:
        print("Invalid input")
