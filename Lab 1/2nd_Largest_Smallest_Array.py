def find_second_largest_and_smallest(arr):
    largest = second_largest = None
    smallest = second_smallest = None
    
    for num in arr:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or largest > num > second_largest:
            second_largest = num
        
        if smallest is None or num < smallest:
            second_smallest = smallest
            smallest = num
        elif second_smallest is None or smallest < num < second_smallest:
            second_smallest = num

    if second_largest is None or second_smallest is None:
        return "There was no second largest or second smallest element."
    
    return second_largest, second_smallest

array = [10, 89, 9, 54, 4, 80, 8]
second_largest, second_smallest = find_second_largest_and_smallest(array)
print("Second Largest:", second_largest)
print("Second Smallest:", second_smallest)