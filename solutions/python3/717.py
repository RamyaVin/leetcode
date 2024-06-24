class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        index = 0
        while index < len(bits):
            if index == len(bits)-1: 
                return True
            if bits[index] == 1: 
                index += 2              
            else: 
                index += 1
        return False
