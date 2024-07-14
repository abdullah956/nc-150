class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for a in s:
            if a.isalpha() or a.isdigit():
                new += a.lower()
        return (new == new[::-1])

# Time Complexity: 
# O(n) for iterating through each character in the string to filter and build the new string `new`.
# O(n) for reversing the string and checking if it is equal to the original `new` string.
# Therefore, the overall time complexity is O(n).

# Space Complexity:
# O(n) for storing the filtered and lowercased characters in the `new` string.
# O(n) for the reversed string created by `new[::-1]` during the palindrome check.
# Therefore, the overall space complexity is O(n).
