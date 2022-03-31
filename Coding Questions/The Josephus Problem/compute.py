# Python3 code to solve the Josephus problem

def get_position(n, k): 
    """
    This is the function that figures out the surviving position of N people recursively.  
    Refer to the program-review text document for more information regarding operation.
    """
    if (n == 1): 
        return 1
    else: 
        # NOTE: The position returned by get_position(n - 1, k) is adjusted
        """
        This is what the below operations means in Python3

        +	Addition	    x + y	
        -	Subtraction	    x - y		
        %	Modulus	        x % y	
        """
        return (get_position(n - 1, k) + k - 1) % n + 1

# Main program
n = int(input('How many people are in the circle today? '))
k = int(input('What is the space between killing each person? '))

print("The chosen place is", get_position(n, k))
