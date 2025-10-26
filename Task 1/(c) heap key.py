# ----- (c) D is stored as heap ----- #

import heapq

def heap(heap, k):
    temp_heap = heap[:]
    heapq.heapify(temp_heap)                # O(n)
    value = None
    for _ in range(k):
        value = heapq.heappop(temp_heap)    # O(k log n)
    return value

# ----- Example ----- #

if __name__ == "__main__":
    D = [38, 10, 3, 8, 25]                  # O(n)
    k = 3

    print("Heap:", heap(D, k))