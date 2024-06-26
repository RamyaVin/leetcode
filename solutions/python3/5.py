class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            while 0 <= left <= right <  < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        longest = ""
        for i in range(len(s)):
            # Odd-length palindrome (centered at i)
            palindrome1 = expand_around_center(i, i)
            # Even-length palindrome (centered between i and i+1)
            palindrome2 = expand_around_center(i, i + 1)

            # Update longest palindrome found so far
            longest = max(longest, palindrome1, palindrome2, key=len)

        return longest
