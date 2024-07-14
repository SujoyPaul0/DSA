def permutation_sort(A):
    '''Sort A'''
    for B in permutations(A):   # O(n!)
        if is_sorted(B):        # O(n)        
            return B            # O(1)