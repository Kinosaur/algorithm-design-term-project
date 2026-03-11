import sys

def solve_interval_dp(exercises):
    E = len(exercises)
    W = len(exercises[0])

    # Precompute shared_weights[i][j] for all intervals
    # shared_weights[i][j] = sum of per-type minimums across exercises[i..j]
    shared_weights = [[0] * E for _ in range(E)]
    for i in range(E):
        # Start with just exercise i
        mins = list(exercises[i])
        shared_weights[i][i] = sum(mins)
        # Extend interval rightward
        for j in range(i + 1, E):
            for w in range(W):
                mins[w] = min(mins[w], exercises[j][w])
            shared_weights[i][j] = sum(mins)

    # dp[i][j] = minimum cost to complete exercises[i..j]
    dp = [[0] * E for _ in range(E)]

    # Base case: single exercise
    for i in range(E):
        dp[i][i] = 2 * sum(exercises[i])

    # Fill by increasing interval length
    for length in range(2, E + 1):           # length of interval
        for i in range(E - length + 1):      # start index
            j = i + length - 1              # end index

            savings = 2 * shared_weights[i][j]
            best_cost = float('inf')

            # Try every split point k
            for k in range(i, j):
                total_cost = dp[i][k] + dp[k + 1][j] - savings
                if total_cost < best_cost:
                    best_cost = total_cost

            dp[i][j] = best_cost

    return dp[0][E - 1]

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])
    idx = 1

    for t in range(1, T + 1):
        E = int(input_data[idx])
        W = int(input_data[idx + 1])
        idx += 2

        exercises = []
        for _ in range(E):
            ex = [int(input_data[idx + w]) for w in range(W)]
            idx += W
            exercises.append(ex)

        ans = solve_interval_dp(exercises)
        print(f"Case #{t}: {ans}")

if __name__ == '__main__':
    main()