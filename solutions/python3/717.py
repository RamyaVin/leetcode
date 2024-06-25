class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                i += 2
                if i > len(bits):
                    return False
            else:
                if i == len(bits)-1:
                    return True
                i += 1
