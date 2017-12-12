#!/bin/python3

actual = input()
expected = input()

a_data = actual.split()
e_data = expected.split()
# Split to day month year
da = int(a_data[0])
ma = int(a_data[1])
ya = int(a_data[2])
de = int(e_data[0])
me = int(e_data[1])
ye = int(e_data[2])

fine = 0
# Over a year late
if ya > ye:
    fine = 10000
# Same year
elif ya == ye:
    # Months late
    if ma > me:
        fine = 500 * (ma - me)
    # Same month
    elif ma == me:
        # Days late
        if da > de:
            fine = 15 * (da - de)
            
print(fine)
    