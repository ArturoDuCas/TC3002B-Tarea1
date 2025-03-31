class Stack:
    """
    A class that represents a stack (LIFO - Last In, First Out).
    
    ### Attributes:
    - items (list): Internal storage for the stack elements.
    
    ### Methods:
    - isEmpty(): Checks if the stack is empty.
    - push(item): Adds an item to the top of the stack.
    - pop(): Removes and returns the item at the top of the stack.
    - peek(): Returns the item at the top of the stack without removing it.
    - size(): Returns the number of elements in the stack.
    """
    
    def __init__(self):
        self.items = []

    def isEmpty(self):
        """
        Checks if the stack is empty.
        
        ### Returns:
        - bool: True if the stack is empty, False otherwise.
        """
        
        return len(self.items) == 0

    def push(self, item):
        """
        Adds an item to the top of the stack.
        
        ### Parameters:
        - item: The element to be added to the stack.
        
        ### Returns:
        - None
        """
        
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the item at the top of the stack.
        
        ### Returns:
        - The element that was removed from the stack.
        """
        
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        """
        Returns the item at the top of the stack without removing it.
        
        ### Returns:
        - The element at the top of the stack.
        """
        
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        """
        Returns the number of elements in the stack.
        
        ### Returns:
        - int: The count of elements in the stack.
        """
        return len(self.items)

    def __str__(self):
        return str(self.items)