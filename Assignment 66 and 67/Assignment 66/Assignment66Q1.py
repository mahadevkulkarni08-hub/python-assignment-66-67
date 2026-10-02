#inputs
import math


x1 = 2
x2 = 3
w1 = 0.4
w2 = 0.6

bias = 0.5


Weighted_sum = (x1 * w1) + (x2 * w2) + bias


sigmoid = 1 / (1 + math.exp(-Weighted_sum))

# 3. Display results
print("Weighted Sum:", Weighted_sum)
print("Sigmoid Output:", sigmoid)

# 4. Interpretation
if sigmoid >= 0.5:
    print("Output is close to 1 (High Activation)")
else:
    print("Output is close to 0 (Low Activation)")