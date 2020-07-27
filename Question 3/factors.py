def getFactors(n):
    # Create an empty list for factors
    factors=[];

    # Loop over all factors
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    # Return the list of factors
    return factors

# Call the function with a given value
print ('Banyak bilangan faktor dari 262144 : ' + str(len(getFactors(262144))))
print ('Banyak bilangan faktor dari 134217728 : ' + str(len(getFactors(134217728))))