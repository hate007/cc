numbers = []
count = int(input("Enter the number of inputs (up to 5): "))
if count > 10:
    count = 10
for i in range(count):
    number = float(input(f"Enter number {i + 1}: "))
    numbers.append(number)
average = sum(numbers) / len(numbers)
print(f"The average is: {average}")
