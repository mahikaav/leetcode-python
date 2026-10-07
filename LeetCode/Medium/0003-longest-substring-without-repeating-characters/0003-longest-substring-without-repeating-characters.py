class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        counter = {}
        max_count = 0

        for end in range(len(s)):
            counter[s[end]] = counter.get(s[end],0) + 1

            while len(counter) < end - start + 1:
                counter[s[start]]  -= 1
                if counter[s[start]] == 0:
                    del counter[s[start]]
                start += 1
            max_count = max(max_count,end-start + 1)

        return max_count