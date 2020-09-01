class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.length = 0

        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0:
            return -1
        it = self.head
        for i in range(index):
            it = it.next
            if it is None:
                return -1
        return it.val

        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head is not None:
            temp = self.head
            self.head = Node(val, next=temp)
            temp.prev = self.head
        else:
            self.head = Node(val)
            self.tail = self.head
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.tail is not None:
            self.tail.next = Node(val, prev=self.tail)
            self.tail = self.tail.next
        else:
            self.tail = Node(val)
            self.head = self.tail
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.length:
            self.addAtTail(val)
            return
        it = self.head
        for i in range(index):
            it = it.next
        newNode = Node(val, prev=it.prev, next=it)
        it.prev.next = newNode
        it.prev = newNode
        self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
        elif index == self.length-1:
            self.tail = self.tail.prev
            if self.tail is not None:
                self.tail.next = None
        else:
            it = self.head
            for i in range(index):
                it = it.next
            it.prev.next = it.next
            it.next.prev = it.prev
        self.length -= 1


    def __str__(self):
        output = ""
        it = self.head
        while it is not None:
            output += str(it.val)
            if it.next is not None:
                output += " -> "
            it = it.next
        return output
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# test driver

linkedList = MyLinkedList()
linkedList.addAtHead(1)
# linkedList.deleteAtIndex(0)
print(linkedList)
print("GET INDEX 2:", linkedList.get(0))
print("GET HEAD:", str(linkedList.head.val))
print("GET TAIL:", str(linkedList.tail.val))