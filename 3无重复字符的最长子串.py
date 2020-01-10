class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp = ''
        count = 0
        end = 0
        for a in s:
            if a in tmp:
                print(tmp)
                tmp = a
                end = len(tmp)
                print()
                if end < count:
                    end = count
                count = 0
            else:
                count += 1
                tmp = tmp + a
        if end < count:
            end = count
        return end


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("pwwkew"))
