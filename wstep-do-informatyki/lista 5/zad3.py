def iterative_gcd(n, m):
    # Initially set the factor of 2 to 1 (2^0)
    factor_of_2 = 1
    
    # Continue the loop until one of the numbers becomes 0
    while n != 0 and m != 0:
        # If both numbers are even, divide both by 2 and update the factor of 2
        if n % 2 == 0 and m % 2 == 0:
            n //= 2
            m //= 2
            factor_of_2 *= 2
        # If n is even and m is odd, divide n by 2
        elif n % 2 == 0:
            n //= 2
        # If n is odd and m is even, divide m by 2
        elif m % 2 == 0:
            m //= 2
        # If both numbers are odd, reduce the larger number
        elif n > m:
            n = (n - m)
        else:
            m = (m - n)
    
    # When either n or m is 0, the other contains the gcd
    gcd = max(n, m)
    
    # Multiply by the factor of 2 to get the final gcd
    return gcd * factor_of_2

print(iterative_gcd(2, 10))