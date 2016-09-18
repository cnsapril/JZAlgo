class Solution:
    def findMissing2(self, n, str1):
        # Write your code here
        def helper(str1, visited):
            if not str1:
                if False not in visited:
                    return True
                else:
                    return False

            digit1, digit2 = int(str1[0]) - 1, None
            if digit1 == -1:
                return False
            if len(str1) > 1:
                digit2 = int(str1[:2]) - 1
                if digit2 + 1 > n:
                    digit2 = None

            if not visited[digit1]:
                visited[digit1] = True
                result = helper(str1[1:], visited)
                if result:
                    return True
                else:
                    visited[digit1] = False

            if digit2 is not None and not visited[digit2]:
                visited[digit2] = True
                result = helper(str1[2:], visited)
                if result:
                    return True
                else:
                    visited[digit2] = False

            return False

        for i in range(n):
            visited = [False for x in range(n)]
            visited[i] = True
            if helper(str1, visited):
                return i + 1


sol = Solution()

print sol.findMissing2(20, "19201234567891011121314151618")
