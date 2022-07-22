class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        
    def print_stack(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            while temp is not None:
                print(temp.value)
                temp = temp.next
                
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
    
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        if self.height == 1:
            self.top == None
        else:
            self.top = temp.next
            temp.next = None
        self.height -= 1
        return temp        
        
                        
my_stack = Stack(0)
my_stack.push(1)
my_stack.pop()
my_stack.print_stack()