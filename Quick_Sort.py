def partition(arr, start_element, end_element):
    pivot = arr[end_element]
    i = start_element - 1

    for j in range(start_element, end_element):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end_element] = arr[end_element], arr[i + 1]
    return i + 1

def quicksort(arr, start_element, end_element):
    if start_element < end_element :

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
