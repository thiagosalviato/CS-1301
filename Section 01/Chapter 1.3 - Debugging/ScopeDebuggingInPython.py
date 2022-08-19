print("Calculating...")
grades = [100, 95, 93, 91, 90, 89, 87, 87, 85, 85, 84, 82]
sum = 0
count = 0
for grade in grades:
    count = count + 1
    sum = sum + grade
    print("Current sum", sum)
print(sum / count)
