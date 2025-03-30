class Dictionary:
    """
    A class to represent a simple dictionary-like data structure.
    
    ### Attributes:
    - data (dict): Internal storage for the dictionary.
    
    ### Methods:
    - __init__(): Initializes the Dictionary object with an empty data dictionary.
    - insert(key, value): Inserts a key-value pair into the dictionary.
    - get(key): Retrieves the value associated with the given key.
    - delete(key): Deletes a key-value pair from the dictionary.
    - __str__(): Returns a string representation of the dictionary.
    """
    def __init__(self):
        self.data = {}
    
    
    def insert(self, key, value):
        """
        Inserts a key-value pair into the dictionary.
        
        ### Parameters:
        - key: The key to insert.
        - value: The value associated with the key.
        
        ### Returns:
        - None
        """
        self.data[key] = value
    
    def get(self, key):
        """
        Retrieves the value associated with the given key.
        
        ### Parameters:
        - key: The key whose value is to be retrieved.
        
        ### Returns:
        - The value associated with the key, or None if the key does not exist.
        """
        return self.data.get(key, None)
    
    
    def delete(self, key):
        """
        Deletes a key-value pair from the dictionary.
        
        ### Parameters:
        - key: The key to delete.
        
        ### Returns:
        - None        
        """
        if key in self.data:
            del self.data[key]
        else:
            print(f"Key '{key}' not found in dictionary.")

    def __str__(self):
        return str(self.data)