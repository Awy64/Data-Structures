"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        if (self.head == None and self.tail == None):
          self.length += 1
          self.head = new_node
          self.tail = new_node
        else:
          self.length += 1
          self.head.prev = new_node
          new_node.next = self.head
          self.head = new_node

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if (self.head == None and self.tail == None):
          return None
        elif(self.head == self.tail):
          value = self.head.value
          self.head = None
          self.tail = None
          self.length -= 1
          return value
        else:
          value = self.head.value
          self.head = self.head.next
          self.head.prev = None
          self.length -= 1
          return value
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if (self.head == None and self.tail == None):
          self.head = new_node
          self.tail = new_node
          self.length += 1
        else:
          self.tail.next = new_node
          new_node.prev = self.tail
          self.tail = new_node
          self.length += 1
          
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if (self.head == None and self.tail == None):
          return None
        elif (self.head == self.tail):
          value = self.tail.value
          self.head = None
          self.tail = None
          self.length -= 1
          return value
        else:
          value = self.tail.value
          self.tail = self.tail.prev
          self.tail.next = None
          self.length -= 1
          return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if (self.head == None and self.tail == None):
          return None
        elif (self.head == self.tail):
          return None
        elif (self.head == node):
          return None
        elif (self.tail == node):
          current_node = self.tail
          self.tail = self.tail.prev
          self.tail.next = None
          self.head.prev = current_node
          current_node.next = self.head
          self.head = current_node
        else:
          current_node = self.head
          while current_node != node:
            current_node = current_node.next
          next_node = current_node.next
          prev_node = current_node.prev
          prev_node.next = current_node.next
          next_node.prev = current_node.prev
          current_node.next = self.head
          self.head.prev = current_node
          current_node.prev = None
          self.head = current_node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if (self.head == None and self.tail == None):
          return None
        elif (self.head == self.tail):
          return None
        elif (self.tail == node):
          return None
        elif (self.head == node):
          current_node = self.head
          self.head = self.head.next
          self.head.prev = None
          self.tail.next = current_node
          current_node.prev = self.tail
          self.tail = current_node
        else:
          current_node = self.head
          while current_node != node:
            current_node = current_node.next
          next_node = current_node.next
          prev_node = current_node.prev
          prev_node.next = current_node.next
          next_node.prev = current_node.prev
          current_node.prev = self.tail
          self.tail.next = current_node
          current_node.next = None
          self.tail = current_node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if (self.head is None and self.tail is None):
          return None
        elif (self.head is self.tail):
          self.head = None
          self.tail = None
          self.length = 0
        elif (self.head == node):
          self.head = self.head.next
          self.head.prev = None
          self.length -= 1
        elif (self.tail == node):
          self.tail = self.tail.prev
          self.tail.next = None
          self.length -= 1
        else:
          current_node = self.head
          while current_node != node:
            current_node = current_node.next
          next_node = current_node.next
          prev_node = current_node.prev
          prev_node.next = next_node
          next_node.prev = prev_node
          current_node.next = None
          current_node.prev = None
          self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        x = 0
        y = 0
        current_node = self.head
        while x != self.length:
          value = current_node.value
          if (y < value):
            y = value
          else:
            pass
          # if current_node == self.tail:
          #   break
          current_node = current_node.next
          x += 1
        return y
        
