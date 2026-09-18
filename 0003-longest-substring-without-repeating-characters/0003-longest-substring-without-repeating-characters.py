class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_characters = set()
        left_pointer = 0
        max_length = 0

        for right_pointer in range(len(s)):

            while s[right_pointer] in seen_characters:
                seen_characters.remove(s[left_pointer])
                left_pointer += 1

            seen_characters.add(s[right_pointer])

            current_window_length = right_pointer - left_pointer + 1
            max_length = max(max_length, current_window_length)

        return max_length
                

        