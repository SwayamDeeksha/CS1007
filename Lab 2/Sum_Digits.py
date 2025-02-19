def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

num = int(input("Enter a number:"))
result = sum_of_digits(num)

print(f"The sum of digits of the number {num} is {result}")