def longestCommonSubstring(s1, s2):
    len1 = len(s1)
    len2 = len(s2)

    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    max_length = 0

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])

    return max_length

s1 = input("Enter 1st String")
s2 = input("Enter 2nd String")
result = longestCommonSubstring(s1, s2)
print("Length of Longest Common Substring:", result)
