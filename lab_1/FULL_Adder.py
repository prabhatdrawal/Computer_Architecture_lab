A = int(input("enter binary bit value 0 or 1"))
B = int(input("enter binary bit value 0 or 1"))
C = int(input("enter binary bit value 0 or 1"))


sum = (A^B^C)
carry = (A&B | B&C | C&A)
print(f"sum = {sum}"f" and carry = {carry}") 