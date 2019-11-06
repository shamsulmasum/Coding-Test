# -*- coding: utf-8 -*-

def count_number_of_ways(n):
    """ count number of ways to represent sum n """
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    dp = [[0] * len(coins) for i in range(n + 1)]

    # we can represent sum 0 in only one way
    for i in range(len(coins)):
        dp[0][i] = 1

    # fill up dp table
    for s in range(1, n + 1):
        # number of ways to represent sum s using 1p coin
        dp[s][0] = 1

        # calculate for sum s using 0...i coins
        for i in range(1, len(coins)):
            dp[s][i] = dp[s][i - 1]

            p = s - coins[i]
            while p >= 0:
                dp[s][i] = dp[s][i] + dp[p][i - 1]
                p = p - coins[i]

    return dp[n][-1]

if __name__ == "__main__":
    print(count_number_of_ways(200))


