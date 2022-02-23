class Node:
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):  
    self.head = None
  
  def insert(self, data):
    newNode = Node(data)
    if self.head:
      current = self.head
      while current.next:
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  def printLL(self):
    current = self.head
    while current:
      print(current.data, "--> ", end='')
      current = current.next

def sorted_linked_list(llist):
  current = llist.head
  if current == None and current.next == None:
    return

  while current.next:
    if current.data == current.next.data:
      current.next = current.next.next      
    else:
      current = current.next
     
  return llist

LL = LinkedList()
LL.insert(1)
LL.insert(1)
LL.insert(3)
LL.insert(4)
LL.insert(4)
LL.insert(5)
LL.insert(6)
LL.insert(6)

sorted_llist = sorted_linked_list(LL)
sorted_llist.printLL()

'''
  Algorithm: if the current node and the next node is None, the linked list is empty.
  Initialise a while loop till the second last node of the linkedlist.
  If the data of current and next node is equal we will skip the node between them.
  If the data of current and next node is different move the pointer to the next node.
  Finally return the new sorted linked list.

  Complexity: O(n)
'''