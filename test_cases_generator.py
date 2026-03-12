import random

def generate_large_test_cases(filename="large_test5.in"):
    # Target number of test cases
    T = 100
    
    with open(filename, 'w') as f:
        f.write(f"{T}\n")
        
        for _ in range(T):
            # E: number of exercises (Randomized between 10 and 100)
            E = random.randint(10, 100) 
            
            # W: number of weight types (Code Jam limits are W <= 100 for Test Set 2)
            W = random.randint(1, 100)
            
            f.write(f"{E} {W}\n")
            
            for _ in range(E):
                # Each exercise needs W integers between 0 and 100
                weights = [random.randint(0, 100) for _ in range(W)]
                
                # Problem constraint: Each exercise requires at least one weight
                if sum(weights) == 0:
                    weights[random.randint(0, W - 1)] = random.randint(1, 100)
                    
                # Write the row of weights separated by spaces
                f.write(" ".join(map(str, weights)) + "\n")

if __name__ == "__main__":
    generate_large_test_cases()
    print("Generated 'large_test.in' successfully!")