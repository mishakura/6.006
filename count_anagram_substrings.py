def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    A = []
    ##################
    # YOUR CODE HERE #
    ##################
    for k in range(len(S)):
        wordLength = len(S[k])
        wordHash, anagramHash = {} , {}
        for i in range(len(S[k])):
            wordHash[S[k][i]] = 1 + wordHash.get(S[k][i], 0)
            anagramHash[T[i]] = 1 + anagramHash.get(T[i], 0)
    
        ans = 1 if wordHash == anagramHash else 0

        for i in range(1,len(T) - wordLength):
            anagramHash[T[i - 1]] = - 1 + anagramHash.get(T[i - 1], 0)
            if anagramHash[T[i - 1]] <= 0:
                del anagramHash[T[i - 1]]
            anagramHash[T[i + (wordLength - 1)]] = 1 +anagramHash.get(T[i + (wordLength - 1)], 0)
            if anagramHash == wordHash:
                ans += 1
        A.append(ans)
    return A

