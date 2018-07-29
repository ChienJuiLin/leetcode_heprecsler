class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        r_digits = digits[::-1]
        carry = 0

        r_digits[0] = r_digits[0] + 1

        if r_digits[0] >= 10:
            r_digits[0] = 0
            carry = 1

        n = 1

        while carry != 0:
            if n < len(r_digits):
                r_digits[n] = r_digits[n] + 1
                if r_digits[n] == 10:
                    r_digits[n] = 0
                    carry = 1
                    n = n + 1
                else:
                    carry = 0
            else:
                r_digits.append(1)
                carry = 0

        return r_digits[::-1]

# 最後一行直接從前面加挺快的
'''
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            sum = digits[i]
            if i == len(digits) - 1: sum += 1
            else: sum += carry
            digits[i] = sum % 10
            carry = int(sum / 10)
            if carry == 0: break

        return digits if carry == 0 else [1] + digits
'''
