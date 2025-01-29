# Define the function
def largest_smallest(arr):
    largest = smallest = arr[0]
    
    for num in arr:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    
    return largest, smallest

arr = [10, 89, 9, 56, 4, 80, 8]
largest, smallest = largest_smallest(arr)
print(f"Largest number = {largest}")
print(f"Smallest number = {smallest}")
