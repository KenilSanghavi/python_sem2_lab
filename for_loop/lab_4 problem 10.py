N = 10  # Example value
a, b = 0, 1
for _ in range(N):
    print(a, end=" ")
    a, b = b, a + b
