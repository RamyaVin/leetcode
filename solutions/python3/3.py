class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}  # Store character indices
        start = 0  # Start of the sliding window
        max_length = 0

        for i in range(len(s)):
            if s[i] in chars and chars[s[i]] >= start:
                start = chars[s[i]] + 1
            chars[s[i]] = i
            max_length = max(max_length, i - start + 1)

        return max_length
