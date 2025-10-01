def greedy_rep(coins, amount): #ChatGPT
    """
    Return the greedy representation of `amount` using `coins`,
    as a list of counts aligned with the coins list.
    coins: sorted in descending order, coins[0] > coins[1] > … > coins[-1] = 1
    """
    rep = []
    rem = amount
    for c in coins:
        cnt = rem // c #uses Division algorithm
        rep.append(cnt)
        rem -= cnt * c
    # since 1 is coin[-1], rem should end at 0
    return rep

def pearson_is_canonical(coins):
    """
    Returns (is_canonical: bool, counterexample_amount or None)
    Implements Pearson’s O(n^3) algorithm to check if the coin system `coins`
    is canonical; coins must include 1, and be sorted descending.
    """
    n = len(coins)
    # sanity checks
    if coins[-1] != 1:
        # no coin of value 1: can't represent all amounts
        return False, None

    # For each pair (i, j) with 1 < i <= j <= n
    # We number coins by: coins[0] is largest, coins[n-1] = 1 (smallest).
    for i in range(1, n):          # i from 1 to n-1 (0-based indexing)
        for j in range(i, n):      # j from i to n-1
            # Step 1: compute G(c_{i-1} - 1)
            x = coins[i - 1] - 1
            G_x = greedy_rep(coins, x)

            # Step 2: build candidate minimal representation M_w
            # As per Pearson: take the first j entries of G_x, but in the j-th entry, add 1;
            # drop everything from j+1 onward (set them to zero).
            M_w = list(G_x)  # copy
            # (entries up to index j-1 are the same)
            # increment j-th entry:
            M_w[j] += 1
            # zero out entries after j
            for k in range(j + 1, n):
                M_w[k] = 0

            # Step 3: compute the candidate amount w from M_w
            # w = sum over coins[k] * M_w[k]
            w = sum(coins[k] * M_w[k] for k in range(n))

            # compute greedy representation on w
            G_w = greedy_rep(coins, w)

            # compare number of coins: is greedy worse than M_w?
            if sum(G_w) > sum(M_w):
                # counterexample found
                return False, w

    # If none of these candidates yields greedy strictly worse,
    # the system is canonical
    return True, None


# Example usage
if __name__ == "__main__":
    coins_US = [25, 10, 5, 1]        # canonical
    print(pearson_is_canonical(coins_US))  # (True, None)

    coins_list2 = [25, 10, 1]       # no nickel
    print(pearson_is_canonical(coins_list2))  
    # expects something like (False, w) for some counterexample w
    coins_Korean = [500,100,50,10,5,1]
    print(pearson_is_canonical(coins_Korean)) 
