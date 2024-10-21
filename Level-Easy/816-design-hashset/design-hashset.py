class MyHashSet:
    def __init__(self):
        # Initialize an array of empty lists (buckets), we use 1000 for simplicity
        self.size = 1000
        self.data = [[] for _ in range(self.size)]
    
    def hash(self, key: int) -> int:
        # A simple hash function that maps a key to an index
        return key % self.size
    
    def add(self, key: int) -> None:
        # Add the key to the appropriate bucket, if not already present
        index = self.hash(key)
        if key not in self.data[index]:
            self.data[index].append(key)
    
    def remove(self, key: int) -> None:
        # Remove the key from the bucket, if it exists
        index = self.hash(key)
        if key in self.data[index]:
            self.data[index].remove(key)
    
    def contains(self, key: int) -> bool:
        # Check if the key is in the appropriate bucket
        index = self.hash(key)
        return key in self.data[index]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)