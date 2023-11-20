def knapSack(BagLimit, wt, profit, n):

    K = [[0 for x in range(BagLimit + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(BagLimit + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(profit[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                # same as previous
                K[i][w] = K[i-1][w]

    return K[n][BagLimit]


# Driver code
if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    BagLimit = 50
    n = len(profit)
    print(knapSack(BagLimit, weight, profit, n))