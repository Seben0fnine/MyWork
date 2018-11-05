import numpy as np

n = 20  # Number of elements in the array
# Generate a random array of 200 integers within range [0, 100]
a = np.random.randint(100, size=n)
print (a)
for i in range(n - 1):
    if a[i] >= a[i + 1]:
        print("Peak is {} at position {}".format(a[i], i))
        break
    elif i == n-2:
        print("Peak is {} at position {}".format(a[i+1], i+1))
