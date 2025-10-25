import heapq

# ----- (a) D as sorted array ----- #

def sorted_array(array, k):
    if k < 1 or k > len(array):
        raise ValueError("[ERROR]: k is out of bounds.")
    return array[k - 1]

# ----- (b) D as linked list ----- #

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def linked_list(head, k):
    current = head
    count = 1
    while current:
        if count == k:
            return current.key
        current = current.next
        count += 1
    raise ValueError("[ERROR]: k is out of bounds.")

def build_linked_list(sorted_keys):
    head = Node(sorted_keys[0])
    current = head
    for key in sorted_keys[1:]:
        current.next = Node(key)
        current = current.next
    return head
    
# ----- (c) D as heap ----- #
def heap(heap, k):
    if k < 1 or k > len(heap):
        raise ValueError("[ERROR]: k is out of bounds.")
    temp_heap = heap[:]
    heapq.heapify(temp_heap)
    val = None
    for _ in range(k):
        val = heapq.heappop(temp_heap)
    return val

# ----- Usage ----- #
if __name__ == "__main__":
    D = [3, 1, 5, 2, 4]
    k = 3

    # (a)
    D_sorted = sorted(D)
    print("Array", sorted_array(D_sorted, k))

    # (b)
    D_linked = build_linked_list(D_sorted)
    print("Linked List:", linked_list(D_linked, k))

    # (c)
    D_heap = D[:]
    heapq.heapify(D_heap)
    print("Heap:", heap(D_heap, k))