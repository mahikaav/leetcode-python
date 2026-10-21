class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        n = len(temperatures)
        result = [0]*n

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                gone = stack.pop()
                result[gone] = i - gone
            stack.append(i)
        return result