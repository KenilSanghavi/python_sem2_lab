n = 153  # Example number

# Prime
is_prime = True
if n <= 1:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

# Perfect
sum_factors = sum(i for i in range(1, n) if n % i == 0)
is_perfect = sum_factors == n

# Armstrong
digits = [int(d) for d in str(n)]
length = len(digits)
is_armstrong = sum(d ** length for d in digits) == n

# Palindrome
s = str(n)
is_palindrome = s == s[::-1]

# Automorphic
square = n * n
is_automorphic = str(square).endswith(str(n))

print(f"Prime: {is_prime}")
print(f"Perfect: {is_perfect}")
print(f"Armstrong: {is_armstrong}")
print(f"Palindrome: {is_palindrome}")
print(f"Automorphic: {is_automorphic}")
