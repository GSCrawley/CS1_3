from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        if self.list.head == None:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        node_count = 0
        if self.list.size == 0:
            return node_count
        else:
            print("Size: ",self.list.size)
            return self.list.size

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Push given item
        if self.list.head == None:
            self.list.append(item)
        else:
            self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if self.is_empty() == True:
            return
        else:
            return self.list.tail.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any

        if self.is_empty() == True:
            print("test")
            raise ValueError
        else:
            popped = self.list.tail.data
            self.list.delete(self.list.tail.data)
            return popped

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
        if len(self.list) == 0:
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
        # TODO: Insert given item
        return self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if len(self.list) == 0:
            return None

        return self.list[len(self.list) -1]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any
        if self.is_empty() == True:
            raise ValueError
        if len(self.list) == 0:
            return
        else:
            print(len(self.list)-1)
            popped = self.list[-1]
            self.list.pop(len(self.list)-1)
        return popped


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack

Stack = ArrayStack
# Stack.push(1)
# Stack.push(4)
# Stack.push(9)
print(Stack)