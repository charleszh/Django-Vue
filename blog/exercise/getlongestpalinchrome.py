class Solution(object):
    def get_longest_palin_drome(self, s):
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i+1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len-1)//2
                end = i + max_len//2
        return s[start:end+1]

    def expand(self, s, left, right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left -= 1
            right += 1
        return right-left-1


if __name__ == "__main__":
    str1 = "abcabcdcba"
    result = Solution().get_longest_palin_drome(str1)
    print(result)
