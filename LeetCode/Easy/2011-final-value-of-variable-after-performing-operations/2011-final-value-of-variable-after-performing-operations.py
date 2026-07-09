class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for var in operations:
            if (var == "--X" or var =="X--"):
                x=x-1
            elif (var == "X++" or var == "++X"):
                x=x+1
        return x