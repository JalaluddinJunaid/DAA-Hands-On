# The quicksort logic in this code selects a random element as pivot element and then sorts the array using it.

import random as randpiv

def random_pivot_quicksort(array):
    if len(array) <= 1:
        return array
    pivot = randpiv.choice(array)
    smaller = [x for x in array if x < pivot]
    equals = [x for x in array if x == pivot]
    bigger = [x for x in array if x > pivot]
    return random_pivot_quicksort(smaller) + equals + random_pivot_quicksort(bigger)

# example to understand the working of two different logics
array = [10, 13, 15, 17, 8, 9, 1]
Output_sorted = random_pivot_quicksort(array)
print(Output_sorted)
