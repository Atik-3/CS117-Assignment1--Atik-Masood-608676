


#TASK B2

no_res = int(input("how many resistor "))
if no_res <= 0:
        print("The number of resistors must be greater than zero.")
else:
        total = 0.0
        res = 0.0
        for i in range(1, no_res + 1):
            res= float(input(f"R{i}:"))
            total = total + res
        print("Total resistance: ",total,"ohms")

