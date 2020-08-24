class Solution(object):
    """
    reverse the int instance.
    """
    def reverse(self, num):
        """
        :param num: 123
        :return: 321
        """
        reverse_list = []
        sign = 1 if num > 0 else -1
        abs_num = abs(num)
        while abs_num >= 1:
            reverse_list.append(abs_num%10)
            abs_num = abs_num//10
        i = 0
        res = 0
        while reverse_list:
            res += reverse_list.pop() * 10 ** i
            i += 1
        return res*sign*(res < 2**31)


if __name__ == '__main__':
    num = Solution().reverse(123)
    print(num)
