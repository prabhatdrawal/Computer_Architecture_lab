"""
def full_adder_function():
 A = int(input("enter binary bit value 0 or 1"))
 B = int(input("enter binary bit value 0 or 1"))
 C = int(input("enter binary bit value 0 or 1"))

 sum = (A^B^C)
 carry = (A&B | B&C | C&A)
 print(f"sum = {sum}"f" and carry = {carry}")
 return sum,carry 

full_adder_function()
"""

A_bit = (input("enter first 4 bit data of the value"))
B_bit = (input("enter second four bit data of the value"))
carry = int(0)
result = str( )

for i in range (0,4):
      a_bit = int(A_bit[i])
      b_bit = int(B_bit[i])
      sum_bit = (a_bit ^ b_bit) ^ carry
      new_carry = (a_bit & b_bit) | (carry & a_bit) | (b_bit & carry)

      result = str(sum_bit) + result 
      carry = new_carry


if carry == 1 :
      result = "1"+  result 
      result = str(result)
      overflow = "TRUE"

else:
      overflow = "FALSE"


decimal_sum = int(result,2) # conversion of result to decimal
print(f"sum in binary: {result}")
print(f"sum in decimal: {decimal_sum}")
if overflow == "TRUE":
  print("overflow occured")
else:
     print("no overflow")
     
