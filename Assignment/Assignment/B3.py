


#TASK B3
readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)
count = 0
Sum = 0.0
count = 0
highest = 0
lowest = readings[0]
for r in readings:
    Sum += r
    if r > 3.2:
        count += 1
    if r > highest:
        highest = r
    if r < lowest:
        lowest = r
average = Sum / 7
print(f"Readings above 3.2 V: {count}")
print(f"Highest: {highest} V")
print(f"Lowest: {lowest} V")
print(f"Average: {average:.2f} V")
