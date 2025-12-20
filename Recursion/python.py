# Example 01
def factorial(n):
    if(n==0 or n==1):
        return 1
    return n * factorial(n-1)

# a =int(input("Enter a Number to find a Factorial : "))
# b = factorial(a)
# print(f"The Factorial of given number is {b}")

# Example 01
# 1
# 1+2=3
# 3+3
def sum_pr(n):
    if(n==1):
        return 1
    return sum_pr(n-1) + n 
a = sum_pr(10)
print(a)