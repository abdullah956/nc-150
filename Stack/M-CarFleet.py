from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create a list of tuples (position, speed) and sort by position in descending order
        cars = sorted(zip(position, speed), reverse=True)
        
        # Stack to store times to reach the target
        stack = []
        
        # Calculate time to reach target for each car in reverse sorted order
        for pos, spd in cars:
            time_to_target = (target - pos) / spd
            stack.append(time_to_target)
            
            # Merge fleets if the current car catches up with the previous car
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  # Remove the slower car from the fleet
        
        # Number of fleets is the number of remaining cars in the stack
        return len(stack)
