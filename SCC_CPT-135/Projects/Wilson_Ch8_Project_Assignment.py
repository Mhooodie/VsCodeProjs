'''Chap 7'''

#Question 1
numbers = []
while True:
    num = input("Enter a number or 'exit' to exit to close program: ")
    if num.lower() == 'exit':
        break
    numbers.append(float(num))

squares = [num ** 2 for num in numbers]
print("Squared numbers:", squares)
print("----------------------------------------")





# Question 2
weights = []
for i in range(1, 5):
    weight = float(input(f"Enter weight {i}: "))
    weights.append(weight)

print("Weights:", weights)

average = sum(weights) / len(weights)
print(f"Average weight: {average:.2f}")

max_weight = max(weights)
print(f"Max weight: {max_weight:.2f}")

index = int(input("Enter a number between 1 and 4: "))
if 1 <= index <= 4:
    print(f"Weight at index {index}: {weights[index - 1]:.2f}")
else:
    print("Invalid index.")


sorted_weights = sorted(weights)
print("Sorted weights:", sorted_weights)