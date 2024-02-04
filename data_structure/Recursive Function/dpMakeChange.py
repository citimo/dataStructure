# 用动态规划算法解决找零问题
def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

if __name__ == '__main__':
    c1 = [1, 5, 10, 21, 25]
    coinsUsed = [0]*64
    coinCount = [0]*64
    print(dpMakeChange(c1, 63, coinCount, coinsUsed))
    printCoins(coinsUsed, 63)
    printCoins(coinsUsed, 52)
    print(coinsUsed)
