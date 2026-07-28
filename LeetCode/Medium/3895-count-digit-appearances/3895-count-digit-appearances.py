class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0
        for num in nums:
            while (num > 0):
                dig = num%10
                if dig == digit: count += 1
                num = int(num/10)
        return count