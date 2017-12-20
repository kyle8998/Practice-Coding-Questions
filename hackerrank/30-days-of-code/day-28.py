#!/bin/python3

import sys
import re

gmail = []

N = int(input().strip())
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]

    if re.search(".+@gmail\.com$", emailID):
        gmail.append(firstName)
        
gmail.sort()

for name in gmail:
    print(name)