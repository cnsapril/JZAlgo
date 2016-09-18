class Solution:
    # @param {int} n an integer
    # @return {int} an integer

    def waysNCents(self, n):
        # Write your code here
        def helper(n, total, current, all):
            if total > n:
                return 0
            if total == n:
                if current not in all:
                    all.append(current.copy())
                    return 1
                else:
                    return 0

            current['25'] += 1
            res25 = helper(n, total+25, current, all)
            current['25'] -= 1

            current['10'] += 1
            res10 = helper(n, total+10, current, all)
            current['10'] -= 1

            current['5'] += 1
            res5 = helper(n, total+5, current, all)
            current['5'] -= 1

            current['1'] += 1
            res1 = helper(n, total+1, current, all)
            current['1'] -= 1

            return res25 + res10 + res5 + res1

        return helper(n, 0, {'25': 0, '10': 0, '5': 0, '1': 0}, [])

        # total = 1
        # if n >= 25:
        #     total *= n / 25 * 10
        #     n %= 25
        #     if n >= 10:
        #         total *= n / 10 * 3
        #         n %= 10
        #         if n >= 5:
        #             total *= n / 5 * 3
        #             n %= 5
        #             total *= n
        #         else:
        #             total *= n
        #     elif n >= 5:
        #         total += n / 5 * 3
        #         n %= 5
        #         total += n
        #     else:
        #         total += n
        # elif n >= 10:
        #     total += n / 10 * 3
        #     n %= 10
        #     if n >= 5:
        #         total += n / 5 * 3
        #         n %= 5
        #         total += n
        #     else:
        #         total += n
        # elif n >= 5:
        #     total += n / 5 * 3
        #     n %= 5
        #     total += n
        # else:
        #     total += n
        #
        # return total

sol = Solution()
print sol.waysNCents(50)
