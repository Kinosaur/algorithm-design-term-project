import sys
import time

def get_shared_weights(exercises, start_idx, end_idx):
    """
    Finds the per-type minimum (shared weights) across the interval [start_idx, end_idx].
    """
    if start_idx > end_idx:
        return 0
        
    shared = list(exercises[start_idx])
    
    for i in range(start_idx + 1, end_idx + 1):
        for weight_type in range(len(shared)):
            shared[weight_type] = min(shared[weight_type], exercises[i][weight_type])
            
    return sum(shared)

def solve_memo(exercises, start_idx, end_idx, memo, recursion_counter):
    """
    Memoized recursion. Explores every binary partition of the interval,
    caching results by (start_idx, end_idx) to avoid recomputation.
    """
    recursion_counter["calls"] += 1

    # Return cached result if already computed
    if (start_idx, end_idx) in memo:
        return memo[(start_idx, end_idx)]

    # Base case: Single exercise
    if start_idx == end_idx:
        result = 2 * sum(exercises[start_idx])
        memo[(start_idx, end_idx)] = result
        return result

    # Calculate savings for the global base of this interval
    shared_count = get_shared_weights(exercises, start_idx, end_idx)
    savings = 2 * shared_count

    best_cost = float('inf')

    # Test every split point k
    for k in range(start_idx, end_idx):
        cost_left = solve_memo(exercises, start_idx, k, memo, recursion_counter)
        cost_right = solve_memo(exercises, k + 1, end_idx, memo, recursion_counter)

        # Total Cost = Left + Right - Duplicated Global Base
        total_cost = cost_left + cost_right - savings

        if total_cost < best_cost:
            best_cost = total_cost

    memo[(start_idx, end_idx)] = best_cost
    return best_cost

def main():
    """
    Parses standard input strictly according to the problem specification.
    """
    # Read all tokens from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # Line 1: T (Number of test cases)
    T = int(input_data[0])
    idx = 1

    for t in range(1, T + 1):
        # Read E (Exercises) and W (Weight Types)
        E = int(input_data[idx])
        W = int(input_data[idx+1])
        idx += 2

        # Read the matrix of weight requirements
        exercises = []
        for _ in range(E):
            ex = []
            for _ in range(W):
                ex.append(int(input_data[idx]))
                idx += 1
            exercises.append(ex)

        memo = {}
        recursion_counter = {"calls": 0}

        # Execute the memoized solver for the full sequence [0, E-1]
        start_time = time.perf_counter()
        ans = solve_memo(exercises, 0, E - 1, memo, recursion_counter)
        elapsed_ms = (time.perf_counter() - start_time) * 1000

        print(f"Case #{t}: {ans}")
        print(
            f"[Stats] Case #{t} | Recursions: {recursion_counter['calls']} | Runtime: {elapsed_ms:.3f} ms",
            file=sys.stderr,
        )

if __name__ == '__main__':
    main()