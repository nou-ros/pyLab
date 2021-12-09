'''
Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, 
"pwke" is a subsequence and not a substring.
'''


class Solution:
    def lengthOfLongestSubstring(self, str):
        dicset = {}
        start, result = 0, 0
        for i in range(len(str)):
            if str[i] in dicset:
                start = max(dicset[str[i]], start)
            result = max(result, i-start+1)
            dicset[str[i]] = i+1
            print(dicset)

        return result


sub = Solution()
print(sub.lengthOfLongestSubstring("abcdabcbb"))
