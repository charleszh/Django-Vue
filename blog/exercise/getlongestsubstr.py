class GetLongestSubStr(object):
    """
    Get longest sub string
    """
    def solution(self, str):
        """

        :param str: for example abcbda, abccba, aa, b, abc
        :return: the length of longest sub string
        """
        start = 0
        max_len = 0
        used_char = {}
        for i in range(len(str)):
            if str[i] in used_char and used_char[str[i]] >= start:
                start = used_char[str[i]] + 1
            else:
                max_len = max(max_len, i-start+1)
            used_char[str[i]] = i

        return max_len


if __name__ == "__main__":
    str_exa = 'abcbda'
    max_len = GetLongestSubStr().solution(str_exa)
    print(max_len)
