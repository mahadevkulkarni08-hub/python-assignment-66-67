import math

# Actual and predicted values
actual = [1, 0, 1, 1, 0]
predicted = [0.9, 0.2, 0.8, 0.7, 0.1]

# Mean Squared Error 
mse = sum((a - p) ** 2 for a, p in zip(actual, predicted)) / len(actual)

# Binary Cross Entropy 
bce = -sum(
    a * math.log(p) + (1 - a) * math.log(1 - p)
    for a, p in zip(actual, predicted)
) / len(actual)

# Display results
print("Mean Squared Error:", mse)
print("Binary Cross Entropy:", bce)