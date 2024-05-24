# Quick Sort Algorithm
This repository contains an implementation of the Quick Sort algorithm in Python, with several optimizations for efficiency. Quick Sort is a highly efficient sorting algorithm and is commonly used due to its performance and simplicity.

Features
Median-of-Three Pivot Selection: Chooses the pivot as the median of the first, middle, and last elements to reduce the chance of worst-case time complexity.
Tail Recursion Optimization: Minimizes recursion depth by making a recursive call on the smaller part and iterating over the larger part.
Insertion Sort for Small Arrays: Uses Insertion Sort for subarrays with fewer than 10 elements for better performance on small datasets.
