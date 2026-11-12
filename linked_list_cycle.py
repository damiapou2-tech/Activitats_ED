class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    lent = head
    rapid = head

    while rapid is not None and rapid.next is not None:
        lent = lent.next
        rapid = rapid.next.next

        if lent == rapid:
            return True

    return False
