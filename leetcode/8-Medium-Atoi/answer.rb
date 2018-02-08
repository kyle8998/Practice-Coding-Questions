# @param {String} str
# @return {Integer}
def my_atoi(str)
    sign = 1
    result = 0
    s = 0
    
    # Match string to regex
    if str.match(/^\s*([-+]*\d+)\s*/)
        num = $1
        
        # Loop and check for all leading signs (e.g. '+-+-')
        while not num[s].match(/[0-9]/)
            # If char is a -
            sign *= -1 if num[s] == '-'
            # Just return 0 if more than 1 sign
            # I originally implemented it to account for as many signs as necessary
            return 0 if s == 1
            s += 1
        end
        
        # Loop through the string and append it to the result
        s.upto(num.length-1) do |i|
            result = result*10 + num[i].ord - '0'.ord
        end
    end
    # Sign
    result *= sign
    
    # Returns proper result if result is out of range
    return 2147483647 if result > 2147483647
    return -2147483648 if result < -2147483648
    result
end