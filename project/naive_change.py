import sys
import time

def solve_exact_sequence(exercises):
    """
    Solves the weightlifting problem when weight sequences are strictly ordered.
    'exercises' is a list of lists representing ordered sequences,
    e.g., [[1, 2, 3], [1, 2, 4, 4], [1, 5]].
    
    This function implements the Longest Common Prefix (LCP) logic visualized 
    in Scenarios 1, 2, and 3.
    """
    if not exercises:
        return 0
        
    total_operations = 0
    E = len(exercises)
    
    # 1. Start: Push the entire first exercise sequence onto the empty stack
    total_operations += len(exercises[0])
    
    # 2. Process transitions between adjacent exercises
    for i in range(E - 1):
        # We compare the current exercise sequence with the next one.
        seq_current = exercises[i]
        seq_next = exercises[i + 1]
        
        # We must find how much of the bottom of the stack can be reused.
        # This is the length of their Longest Common Prefix (LCP).
        lcp_len = 0
        for w1, w2 in zip(seq_current, seq_next):
            if w1 == w2:
                lcp_len += 1
            else:
                break
                
        # Pops: We must remove everything above the LCP from the current sequence.
        # If lcp_len is 0, we pop the entire stack.
        pops = len(seq_current) - lcp_len
        
        # Pushes: We must add everything needed for the next sequence onto the LCP.
        # This builds the unique push sequence.
        pushes = len(seq_next) - lcp_len
        
        total_operations += pops + pushes
        
    # 3. End: Pop the entire last exercise sequence to leave the stack empty
    total_operations += len(exercises[-1])
    
    return total_operations

def main():
    """
    Modified input parsing to interpret count-based input as flat sequences.
    Assumes a simple interpretation rule for count data: 
    Weight types are processed 1-indexed (Type 1, Type 2, etc.),
    and we push all counts of Type 1, then all counts of Type 2, etc.
    e.g., Input '2 0 2' (2 of Type 1, 2 of Type 3) -> [1, 1, 3, 3]
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # Line 1: T (Number of test cases)
    try:
        T = int(input_data[0])
    except IndexError:
        return
    idx = 1

    total_start_time = time.perf_counter()
    
    for t in range(1, T + 1):
        # Read E (Exercises) and W (Weight Types)
        try:
            E = int(input_data[idx])
            W = int(input_data[idx+1])
            idx += 2
        except IndexError:
            break
        
        # Modified parsing to create flat, ordered sequences
        exercises_sequences = []
        for _ in range(E):
            current_exercise_seq = []
            for weight_type_1_idx in range(1, W + 1):
                count = int(input_data[idx])
                idx += 1
                # If weight type is present, add it 'count' times in order.
                for _ in range(count):
                    current_exercise_seq.append(weight_type_1_idx)
            exercises_sequences.append(current_exercise_seq)
            
        # Execute the new efficient linear solver
        start_time = time.perf_counter()
        ans = solve_exact_sequence(exercises_sequences)
        elapsed_ms = (time.perf_counter() - start_time) * 1000
        
        # Output in the standard GCJ format
        print(f"Case #{t}: {ans}")
        # Note: We are no longer tracking recursion depth or split points.
        print(
            f"[Stats] Case #{t} | Runtime: {elapsed_ms:.3f} ms",
            file=sys.stderr,
        )

    total_elapsed_ms = (time.perf_counter() - total_start_time) * 1000
    print(
        f"[Total] All {T} test cases completed in {total_elapsed_ms:.3f} ms",
        file=sys.stderr,
    )

if __name__ == '__main__':
    main()