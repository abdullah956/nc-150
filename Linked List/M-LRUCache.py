class Node:
    def __init__(self, key, val):
        # Initialize a node with key, value, and pointers to previous and next nodes
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        # Initialize the LRU cache with a given capacity
        self.cap = capacity
        self.cache = {}  # Dictionary to map keys to their corresponding nodes

        # Create dummy left and right nodes to represent the boundaries of the doubly linked list
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # Remove a node from the doubly linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Insert a node at the right end (most recently used end) of the doubly linked list
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    # Get the value of the key if it exists in the cache, otherwise return -1
    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the accessed node to the right end (most recently used)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    # Insert or update the value of the key, and move the node to the most recently used position
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If the key already exists, remove the old node
            self.remove(self.cache[key])
        # Add the new node to the cache and insert it at the right end
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # If the cache exceeds capacity, remove the least recently used node (left end)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
