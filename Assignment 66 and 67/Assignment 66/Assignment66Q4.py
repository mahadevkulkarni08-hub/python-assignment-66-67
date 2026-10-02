# Input values
x = 2
weight = 0.5
bias = 0.2
target = 1
learning_rate = 0.1

# 1. Calculate prediction
prediction = (x * weight) + bias

# 2. Calculate error
error = target - prediction

# 3. Calculate gradient
gradient = error * x

# 4. Update weight using gradient descent
new_weight = weight + learning_rate * gradient

# Display results
print("Prediction:", prediction)
print("Error:", error)
print("Old Weight:", weight)
print("Updated Weight:", new_weight)