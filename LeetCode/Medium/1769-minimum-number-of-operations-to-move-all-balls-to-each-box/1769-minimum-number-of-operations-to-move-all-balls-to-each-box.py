class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        index_of_ones = []
        n = len(boxes)
        for i in range(n):
            if boxes[i] == '1': index_of_ones.append(i)
        ans = []
        for i in range(n):
            s = 0
            for j in index_of_ones:
                s += abs(i-j)
            ans.append(s)
        return ans