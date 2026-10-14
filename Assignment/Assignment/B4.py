


#TASK B4
voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]
max_length = 1
max_start = voltages[0]
max_end = voltages[0]
current_length = 1
current_start = voltages[0]

for i in range(1, len(voltages)):
    if voltages[i] < voltages[i - 1]:
        if current_length == 1:
            current_start = voltages[i - 1]
        current_length += 1
        current_end = voltages[i]
        if current_length > max_length:
            max_length = current_length
            max_start = current_start
            max_end = current_end
    else:
        current_length = 1
        current_start = voltages[i]

print(f"Longest continuous drop: {max_length} minutes")
print(f"Started at: {max_start} V")
print(f"Ended at: {max_end} V")
