class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node

  def insert_beginning(self, value=None):
    new_node = Node(value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

  def stringify_list(self):
    result = ""
    current_node = self.head_node
    while current_node != None:
      result += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return result

ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())
