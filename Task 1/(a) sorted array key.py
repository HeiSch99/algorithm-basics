# ----- (a) D is stored as sorted array ----- #

def sorted_array(array, k):
    array.sort()            # O(n log n)
    return array[k - 1]     # O(1)

# ----- Example ----- #

if __name__ == "__main__":
    D = [38, 10, 3, 8, 25]  # O(n)
    k = 3

    print("Sorted Array:", sorted_array(D, k))