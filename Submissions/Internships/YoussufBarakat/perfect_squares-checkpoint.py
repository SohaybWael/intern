#1 - Defination : Perfect Square : A perfect square is an integer that is the square of another integer. For example, 1, 4, 9, and 16 are perfect squares because they can be expressed as the square of 1, 2, 3, and 4 respectively.
#2 - The objective : Given an integer n, the objective is to find the least number of perfect square numbers whose sum equals n.
#3 - Example : For example, if n = 12, the least number of perfect square numbers that add up to 12 is 3, because 12 can be expressed as 4 + 4 + 4 (which are all perfect squares). Another valid combination is 9 + 1 + 1 + 1.


def numSquares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  
    for i in range(1, n + 1):
        j = 1
        #print("i = ",i)
        #print("dp[i-1] = ",dp[i-1])
        while j * j <= i:
            #print("j = ",j)
            #print("j^2 = ",j*j)
            #print("dp[i] = ",dp[i])
            #print("dp[i - j^2] = ",dp[i - j*j])
            #print("dp[i - j^2] + 1 = ",dp[i - j*j] + 1)
            # Update the minimum number of perfect squares needed for each number
            dp[i] = min(dp[i], dp[i - j*j] + 1)
            j += 1
            #print("WWWWWWWWWWWWWWWWWWWWW")
        #print("ffffffffffffffffffffffffff")

    return dp[n]

print(numSquares(12))



