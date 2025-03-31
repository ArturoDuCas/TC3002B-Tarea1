class Queue: 
    """
    A class that represents a queue (FIFO - First In, First Out).
    
    ### Attributes:
    - elements (list): Internal storage for the queue elements.
    
    ### Methods:
    - __init__(): Initializes the Queue with an empty list.
    - isEmpty(): Checks if the queue is empty.
    - enqueue(item): Adds an item to the end of the queue.
    - dequeue(): Removes and returns the item at the front of the queue.
    - peek(): Returns the item at the front of the queue without removing it.
    - size(): Returns the number of elements in the queue.
    - __str__(): Returns a string representation of the queue.
    """

    def __init__(self): 
        self.elements = []

    def isEmpty(self): 
        """
        Checks if the queue is empty.
        
        ### Returns:
        - bool: True if the queue is empty, False otherwise.
        """
        
        return len(self.elements) == 0

    def enqueue(self, item):
        """
        Adds an item to the end of the queue.
        
        ### Parameters:
        - item: The element to be added to the queue.
        
        ### Returns:
        - None
        """ 
        self.elements.append(item)
    
    def dequeue(self): 
        """
        Removes and returns the item at the front of the queue.
        
        ### Returns:
        - The element that was removed from the front of the queue.
        """
        
        if not self.isEmpty(): 
            return self.elements.pop(0)
        else: 
            raise IndexError("dequeue from empty queue")
    
    def peek(self): 
        """
        Returns the item at the front of the queue without removing it.
        
        ### Returns:
        - The element at the front of the queue.
        """
        
        if not self.isEmpty(): 
            return self.elements[0]
        else: 
            raise IndexError("peek from empty queue")
    
    def size(self): 
        """
        Returns the number of elements in the queue.
        
        ### Returns:
        - int: The count of elements in the queue.
        """
        return len(self.elements)
    
    def __str__(self): 
        return str(self.elements)