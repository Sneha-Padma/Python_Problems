#Day 16 Detect Cycle in a Linked List
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
def hasCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: 
            return True
    return False

n = int(input().strip())
if n == 0:
    print("false")
else:
    values = list(map(int, input().split()))
    pos = int(input().strip())
    nodes = [ListNode(v) for v in values]
    for i in range(n - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    print("true" if hasCycle(nodes[0]) else "false")
