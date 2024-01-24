def edit_distance(string1, string2):
    len_str1 = len(string1)
    len_str2 = len(string2)

    dp = [[0 for _ in range(len_str2 + 1)] for _ in range(len_str1 + 1)]

    for i in range(len_str1 + 1):
        dp[i][0] = i
    for j in range(len_str2 + 1):
        dp[0][j] = j

    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            cost = 0 if string1[i - 1] == string2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,      
                dp[i][j - 1] + 1,      
                dp[i - 1][j - 1] + cost  
            )

    return dp[len_str1][len_str2]

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
distance = edit_distance(string1, string2)
print(f"The edit distance between '{string1}' and '{string2}' is {distance}")
