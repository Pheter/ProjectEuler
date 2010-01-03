def isPalindrome(x):
    x_reversed = int(str(x)[::-1])
    
    if x == x_reversed:
        return True
    return False

largest_palindrome = None

for i in range(100, 999 + 1):
    for j in range(100, 999 + 1):
        product = i * j
        if isPalindrome(product):
            if product > largest_palindrome:
                largest_palindrome = product

print largest_palindrome