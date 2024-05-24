def partition(arr, start_element, end_element):
    # Select the pivot element (usually the last element)
    pivot = arr[end_element]
    # Initialize the index of the smaller element
    i = start_element - 1

    # Iterate through the array from start_element to end_element - 1
    for j in range(start_element, end_element):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # Move to the next element
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Swap arr[i + 1] and arr[end_element] to place pivot at its correct position
    arr[i + 1], arr[end_element] = arr[end_element], arr[i + 1]
    # Return the partitioning index
    return i + 1

def quicksort(arr, start_element, end_element):
    # Check if there are elements to sort
    if start_element < end_element:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, start_element, end_element)

        # Recursively sort the subarrays on the left and right of the pivot
        quicksort(arr, start_element, pivot_index - 1)
        quicksort(arr, pivot_index + 1, end_element)

# Example for explanation  
arr = [5, 9, 7, 1, 3] 
print("Not Sorted Array:", arr) 
quicksort(arr, 0, len(arr) - 1) 
print("Sorted Array:", arr)
