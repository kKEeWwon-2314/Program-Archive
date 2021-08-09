# Python3 code to solve the Josephus problem

def get_position(N, K): 
    """
    This is the function that figures out the surviving position of N people recursively.  
    Refer to the program-review text document for more information regarding operation.
    """
    if (N == 1): 
        return 1
    else: 
        # NOTE: The position returned by josephus(N - 1, K) is adjusted
        """
        This is what the below operations means in Python3

        +	Addition	    x + y	
        -	Subtraction	    x - y		
        %	Modulus	        x % y	
        """
        return (get_position(N - 1, K) + K-1) % N + 1

# MAIN program
N = int(input('How many people are in the circle today? '))
K = 2

print("The chosen place is", get_position(N, K))
