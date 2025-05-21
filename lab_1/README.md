![2276_4 bit parallel adder](https://github.com/user-attachments/assets/4682eaec-88c8-4f91-9471-c69b6c0934b7) Lab 1: Full Adder and 4-bit Parallel Adder
🎯 Objective
To understand and implement the logic of a 1-bit Full Adder.

To construct a 4-bit Parallel Adder using multiple 1-bit Full Adders.

To simulate and verify the operation using truth tables and Verilog code.

🧠 Theory
🔹 1-Bit Full Adder
A full adder is a combinational circuit that adds three bits:

A (input bit)

B (input bit)

Cin (carry-in)

And it produces two outputs:

Sum

Cout (carry-out)

🧮 Logic Expressions:
Input A	Input B	Carry In (Cin)	Sum	Carry Out (Cout)
0	         0	      0           	0	       0
0          0	      1	            1	       0
0	         1	      0             1	       0
0	         1	      1	            0	       1
1	         0	      0	            1	       0
1          0      	1	            0      	 1
1	         1	      0	            0	       1
1	         1      	1      	      1        1

Boolean Equations:

Sum = A ⊕ B ⊕ Cin

Cout = (A ⋅ B) + (B ⋅ Cin) + (A ⋅ Cin)

🔹 4-Bit Parallel Adder
A parallel adder connects four 1-bit full adders in sequence.
The carry-out of each adder is fed into the carry-in of the next one.

#  Algorithm (Steps)
1. Full Adder Logic
Input: A, B, Cin

Calculate:

sum = A XOR B XOR Cin

carry = (A AND B) OR (B AND Cin) OR (A AND Cin)

2. Parallel Adder Logic
Chain 4 full adders:

Adder 0: inputs A0, B0, Cin = 0 → S0, carry0

Adder 1: inputs A1, B1, Cin = carry0 → S1, carry1

Adder 2: inputs A2, B2, Cin = carry1 → S2, carry2

Adder 3: inputs A3, B3, Cin = carry2 → S3, Cout

📝 Conclusion
This lab demonstrates:

How a 1-bit Full Adder forms the building block of larger arithmetic units.

The chaining logic of parallel adders.

The practical use of Verilog in simulating digital circuits.


