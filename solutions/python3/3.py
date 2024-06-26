class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_list = []
        max_length = 0
        for letter in s:
            # adding letter to list if not present already
            if letter not in letter_list:
                letter_list.append(letter)
            else:
                # if repeatation found, check the length of substring
                if len(letter_list) > max_length:
                    max_length = len(letter_list)
                while True:
                    # removing the characters till repeated character from the start
                    if letter_list.pop(0) == letter:
                        break
                # appending the repeated character
                letter_list.append(letter)
        
        # again checking for max length once scanning of word is complete
        if len(letter_list) > max_length:
            max_length = len(letter_list)
        return max_length

#####################################


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

