class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s): return s
        row, direction, res = 0, -1, [""] * numRows
        for char in s:
            res[row] += char
            if row == 0 or row == numRows - 1: direction *= -1 
            row += direction
        return "".join(res) 

##################copilot##############
def zigzag_conversion(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    
    result = []
    cycle_len = 2 * numRows - 2
    
    for i in range(numRows):
        for j in range(i, len(s), cycle_len):
            result.append(s[j])
            if i != 0 and i != numRows - 1:
                next_j = j + cycle_len - 2 * i
                if next_j < len(s):
                    result.append(s[next_j])
    
    return "".join(result)
