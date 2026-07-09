class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for var in operations:
            if var[1] == "+":
                x= x+1
            else:
                x=x-1
        return x