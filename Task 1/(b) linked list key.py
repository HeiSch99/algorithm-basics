# ----- (b) D is stored as linked list ----- #

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def build_linked_list(sorted_keys):
    head = Node(sorted_keys[0])
    current = head
    for key in sorted_keys[1:]:
        current.next = Node(key)
        current = current.next
    return head

def linked_list(head, k):
    count = 1
    current = head
    while current:                      # O(k)
        if count == k:
            return current.key
        count += 1
        current = current.next

# ----- Example ----- #

if __name__ == "__main__":
    D = [38, 10, 3, 8, 25]              # O(n)
    k = 3

    D_sorted = sorted(D)                # O(n log n)
    D_linked = build_linked_list(D_sorted)
    print("Linked List:", linked_list(D_linked, k))