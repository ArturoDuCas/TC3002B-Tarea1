from dictionary import Dictionary
from stack import Stack
from myQueue import Queue

def stackTests():
    print("Testing Stack Class")
    stack = Stack()

    # Pushing elements onto the stack
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack after pushes:", stack)
    
    # Length of the stack
    print("Length of stack:", stack.size())
    
    # deleting elements from the stack
    print("Popped element:", stack.pop())
    print("Stack after pop:", stack)
    
    # Peeking the top element
    print("Top element:", stack.peek())
    
    # Checking if the stack is empty
    print("Is stack empty?", stack.isEmpty())
    
    # Popping all elements
    while not stack.isEmpty():
        print("Popped element:", stack.pop())
    
    print("Stack after popping all elements:", stack)

def dictionaryTests():
    print("Testing Dictionary Class")
    dictionary = Dictionary()
    
    # Inserting key-value pairs
    dictionary.insert("name", "Arturo")
    dictionary.insert("age", 21)
    
    print("Dictionary:", dictionary)
    print("Get 'name':", dictionary.get("name"))
    print("Get 'age':", dictionary.get("age"))
    
    # Deleting a key
    dictionary.delete("name")
    print("Dictionary after deleting 'name':", dictionary)
    
    # Trying to get a deleted key
    print("Get 'name' after deletion:", dictionary.get("name"))

def queueTests():
    print("Testing Queue Class")
    queue = Queue()
    
    # Enqueuing elements
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Queue after enqueues:", queue)
    
    # Length of the queue
    print("Length of queue:", queue.size())
    
    # Dequeuing elements
    print("Dequeued element:", queue.dequeue())
    print("Queue after dequeue:", queue)
    
    # Peeking the front element
    print("Front element:", queue.peek())
    
    # Checking if the queue is empty
    print("Is queue empty?", queue.isEmpty())
    
    # Dequeuing all elements
    while not queue.isEmpty():
        print("Dequeued element:", queue.dequeue())
    
    print("Queue after dequeuing all elements:", queue)


if __name__ == "__main__":
    print("-" * 20)
    stackTests()
    print("-" * 20)
    dictionaryTests()
    print("-" * 20)
    queueTests()

