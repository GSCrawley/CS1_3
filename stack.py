#!python

from linkedlist import LinkedList

# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests

class LinkedStack(object):

    def __init__(self, iterable=None):
#         """Initialize this stack and push the given items, if any."""
#         # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        return self.list.is_empty()


    def length(self):
#         """Return the number of items in this stack."""
#         # TODO: Count number of items
        return self.list.length


    def push(self, item):
#         """Insert the given item on the top of this stack.
#         Running time: O(???) – Why? [TODO]"""
#         # TODO: Push given item
        return self.list.prepend(item)

    def peek(self):
#         """Return the item on the top of this stack without removing it,
#         or None if this stack is empty."""
#         # TODO: Return top item, if any
        if self.is_empty():
            return None
        else: 
            return self.list.head.data
    
    def pop(self):
#         """Remove and return the item on the top of this stack,
#         or raise ValueError if this stack is empty.
#         Running time: O(???) – Why? [TODO]"""
#         # TODO: Remove and return top item, if any
        if self.is_empty():
            raise ValueError("Cannot pop from an empty stack")
        item = self.list.head.data            
        self.list.delete(item)
        return item


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        if self.length() == 0:
            return True
        else: 
            return False

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if self.is_empty():
            return None
        else:
            return self.list[-1]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any
        if self.is_empty():
            raise ValueError('This stack is empty')
        else:
            return self.peek() and self.list.pop(-1)
    
# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# stack = LinkedStack()
stack = ArrayStack()
stack.push(1)
stack.push(4)
stack.push(5)
print(stack)