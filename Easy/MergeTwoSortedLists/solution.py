# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        output = ""
        while self is not None:
            output += str(self.val)
            if self.next is not None:
                output += "->"
            self = self.next
        return output 


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Merge two sorted lists and return a new sorted list.
    Duplicates are allowed.
    """
    if l1 is None and l2 is None:
        return None
    # initialize head node
    # return head.next as head itself is just a flag as starting point
    head = ListNode()
    ptr = head
    # traverse and compare values
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            # add l1 to list
            ptr.next = l1
            l1 = l1.next
            ptr = ptr.next
        else:
            # add l2 to list
            ptr.next = l2
            l2 = l2.next
            ptr = ptr.next
    while l1 is not None:
        ptr.next = l1
        l1 = l1.next
        ptr = ptr.next
    while l2 is not None:
        ptr.next = l2
        l2 = l2.next
        ptr = ptr.next
    return head.next


def driver():
    """
    Test Driver for mergeTwoLists
    """
    # first list
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    # second list
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    print("Input: %s, %s" %(l1, l2))
    print("Output: %s" %(mergeTwoLists(l1, l2)))


if __name__ == "__main__":
    driver()