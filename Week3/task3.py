def optimal_sequence_alignment_score(sequence1, sequence2, gap_penalty, mismatch_penalty, match_score):
    length1 = len(sequence1)
    length2 = len(sequence2)

    dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]

    for i in range(1, length1 + 1):
        dp[i][0] = i * gap_penalty
    for j in range(1, length2 + 1):
        dp[0][j] = j * gap_penalty

    for i in range(1, length1 + 1):
        for j in range(1, length2 + 1):
            if sequence1[i - 1] == sequence2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + match_score
            else:
                dp[i][j] = max(dp[i - 1][j - 1] + mismatch_penalty,
                               dp[i - 1][j] + gap_penalty,
                               dp[i][j - 1] + gap_penalty)

    return dp[length1][length2]

seq1 = input("Enter the first sequence: ")
seq2 = input("Enter the second sequence: ")
gap_penalty = -2
mismatch_penalty = -1
match_score = 2

alignment_score = optimal_sequence_alignment_score(seq1, seq2, gap_penalty, mismatch_penalty, match_score)
print("Optimal Alignment Score:", alignment_score)
