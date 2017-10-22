from fractions import Fraction

def answer(pegs):
    # your code here
    
    # This code is based off even and odd case formulas
    # if n is even,
    # r0 = -2(p0 - 2(p1 + ... - pn-1) + pn)
    #
    # if n is odd,
    # r0 = -2/3(p0 - 2(p1 + ... - pn-1) + pn)
    
    length = len(pegs)
    
    # If invalid parameter
    if ((not pegs) or length == 1):
        return [-1, 1]
    
    # If the length is odd or even
    if length % 2 == 0: 
        even = True
    else: 
        even = False
    
    # Set result equal to first peg
    result = pegs[0]
    if even: result -= pegs[length - 1]
    else: result += pegs[length - 1]
    
    # Done if length = 2
    if length > 2:
        # Add the rest of the pegs
        for i in range(1, length - 1):
            # Alternate signs
            result += (-1)**i * 2 * pegs[i]
            
    # Python2 doesn't support true division!
    result *= -2
    if even: result = float(result)/3
            
    # Convert to fraction and limit denominator
    frac = Fraction(result).limit_denominator()
    
    # Check if impossible
    curr_radius = frac
    for i in range(0, length - 2):
        dist = pegs[i+1] - pegs[i]
        next_radius = dist - curr_radius
        if (curr_radius < 1 or next_radius < 1):
            return [-1, -1]
        else:
            curr_radius = next_radius
    
    return([frac.numerator, frac.denominator])