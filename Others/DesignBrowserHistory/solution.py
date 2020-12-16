class BrowserHistory:
    """
    A browser history implemented using doubly-linked list
    """
    class Node:
        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self, homepage: str):
        # root is only used as a starting point for __str__ function
        self.root = self.Node(homepage)
        self.current = self.root

    def visit(self, url: str) -> None:
        newPage = self.Node(url, prev=self.current)
        self.current.next = newPage
        self.current = newPage

    def back(self, steps: int) -> str:
        while self.current.prev is not None and steps > 0:
            self.current = self.current.prev
            steps -= 1
        return str(self.current.value)

    def forward(self, steps: int) -> str:
        while self.current.next is not None and steps > 0:
            self.current = self.current.next
            steps -= 1
        return str(self.current.value)

    def __str__(self):
        output = ""
        ptr = self.root
        while ptr is not None:
            output += str(ptr.value)
            if ptr.next is not None:
                output += " => "
            ptr = ptr.next
        return output

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


# driver class
bh = BrowserHistory("leetcode.com")
bh.visit("google.com")
bh.visit("facebook.com")
bh.visit("youtube.com")
print(bh)
print(bh.back(1))
print(bh.back(1))
bh.visit("linkedin.com")
print(bh)
print(bh.forward(2))
print(bh.back(2))
print(bh.back(7))
