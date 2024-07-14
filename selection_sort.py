def selection_sort(A, i = None):            # T(i)
    '''Sort A[:i + 1]'''
    if i is None: i = len(A) - 1            # O(1)            
    if i > 0:                               # O(1)
        j = prefix_max(A, i)                # S(i)
        A[i], A[j] = A[j], A[i]             # O(1)
        selection_sort(A, i - 1)            # T(i - 1)
        
def prefix_max(A, i):                       # S(i)
    '''Return index of maximum in A[:i + 1]'''
    if i > 0:                               # O(1)
        j = prefix_max(A, i - 1)            # S(i - 1)
        if A[i] < A[j]:                     # O(1)
            return j                        # O(1)
    return i                                # O(1)
 
 

 '''
=======
'''

 # prefix_max analysis: Recurrence tree
 # chain of n nodes with Θ(1) work per node, 
 # Summation of (1) from i = 0 to n - 1 = Θ(1)
 
 
 # selection_sort analysis:
 # T(1) = Θ(1),T(n)= T(n − 1) + Θ(n)
 # Substitution: T(n) = Θ(n^2), cn^2 = Θ(n)+ c(n − 1)^2 =⇒ c(2n − 1) = Θ(n)
 # Recurrence tree: chain of n nodes with Θ(i) work per node
 # summation of (i) from i = 0 to n - 1 = Θ(n^2)
 
 '''
 

 '''
=======
'''

Example

Let's go through an example with the list `[3, 1, 4, 1, 5, 9, 2, 6, 5]`.

1. Initial call: `selection_sort([3, 1, 4, 1, 5, 9, 2, 6, 5])`
2. `i` is set to `8` (the last index).
3. `prefix_max` finds the maximum element in the sublist `[3, 1, 4, 1, 5, 9, 2, 6, 5]` (index `5` with value `9`).
4. `9` is swapped with `5` (last element).
5. Recursively call `selection_sort([3, 1, 4, 1, 5, 5, 2, 6, 9], 7)`.
6. Continue this process until the entire list is sorted.

By the end of the recursion, the list will be sorted in ascending order.

'''       