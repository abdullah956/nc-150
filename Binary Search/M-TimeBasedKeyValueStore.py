class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        - keyStore: Dictionary where each key maps to a list of [value, timestamp] pairs.
        
        Time Complexity: O(1) for initialization.
        Space Complexity: O(1) for initialization.
        """
        self.keyStore = {}  # Dictionary to store the key-value-timestamp pairs.

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Store the key with the given value and timestamp.
        
        Time Complexity: O(1) for insertion.
        Space Complexity: O(n) where n is the number of key-value-timestamp pairs stored.
        """
        if key not in self.keyStore:
            self.keyStore[key] = []  # Initialize a list if the key does not exist.
        self.keyStore[key].append([value, timestamp])  # Append the [value, timestamp] pair to the list.

    def get(self, key: str, timestamp: int) -> str:
        """
        Retrieve the value for the given key and timestamp.
        If there are multiple values, return the one with the largest timestamp <= given timestamp.
        If there is no such value, return an empty string.
        
        Time Complexity: O(log n) where n is the number of timestamps for the given key (binary search).
        Space Complexity: O(1) for the search operation.
        """
        res, values = "", self.keyStore.get(key, [])  # Initialize result and get the list of [value, timestamp] pairs.
        l, r = 0, len(values) - 1  # Set the left and right pointers for binary search.
        
        # Perform binary search to find the largest timestamp <= given timestamp.
        while l <= r:
            m = (l + r) // 2  # Calculate the mid-point.
            if values[m][1] <= timestamp:  # Check if the mid-point timestamp is <= given timestamp.
                res = values[m][0]  # Update the result with the value at mid-point.
                l = m + 1  # Move the left pointer to mid + 1.
            else:
                r = m - 1  # Move the right pointer to mid - 1.
                
        return res  # Return the result (empty string if no valid timestamp found).
