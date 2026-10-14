


#TASK A4
a = int(input("Enter bit A: "))
b = int(input("Enter bit B: "))
And = 0
Or = 0
Xor = 0
if (a==0 or a==1) and (b==0 or b==1):
    And = a and b
    Or = a or b
    if a != b:
        Xor=1
    else:
        Xort=0
    print("AND: ",And)
    print("OR: ",Or)
    print("XOR: ",Xor)
else:
    print("Bits must be 0 or 1")
