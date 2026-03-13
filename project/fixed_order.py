import sys

def solve_fixed_order(exercises):
    """
    Solves the problem assuming weights MUST be loaded in strict type order 
    (Type 1, then Type 2, ... Type W).
    Because the order is fixed, no optimization is possible. We just simulate 
    the deterministic transitions. Complexity: O(E * W).
    """
    if not exercises:
        return 0

    total_cost = 0

    # 1. Load the first exercise
    total_cost += sum(exercises[0])

    # 2. Simulate transitions
    for i in range(len(exercises) - 1):
        curr_ex = exercises[i]
        next_ex = exercises[i + 1]
        
        # Calculate the exact physical prefix shared at the bottom of the stack
        shared_prefix_plates = 0
        for w in range(len(curr_ex)):
            # They share plates up to the minimum count of this type
            shared_prefix_plates += min(curr_ex[w], next_ex[w])
            
            # The moment the counts differ, the physical stacks diverge.
            # We cannot share any subsequent weight types.
            if curr_ex[w] != next_ex[w]:
                break
                
        # Operations = (Total plates on bar - Shared) + (Required plates - Shared)
        unload = sum(curr_ex) - shared_prefix_plates
        reload = sum(next_ex) - shared_prefix_plates
        
        total_cost += unload + reload

    # 3. Unload the last exercise
    total_cost += sum(exercises[-1])

    return total_cost

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

        ans = solve_fixed_order(exercises)
        print(f"Case #{t}: {ans}")

if __name__ == '__main__':
    main()