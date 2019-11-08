#!/usr/bin/python3

import sys
import re

vowels = re.compile("[aeiou]")
double = re.compile(r".*(.)\1.*")
combo  = re.compile('.*(ab|cd|pq|xy).*')

def str_test(s):
    # Verify that we have at least 3 vowels
    v = vowels.findall(s)
#    print("Found %d vowels" % len(v))
    if len(v) < 3:
        return (False, "Too few vowels")
    
    # Verify no double letters
    d = double.match(s)
    if d:
        None
#        print("Found double %s" % d.group(1))
    else:
#        print("No doubles")
        return (False, "No doubles")
        
    # Verify forbidden combos
    c = combo.match(s)
    if c:
#        print("Found forbidden combo %s" % c.group(1))
        return (False, "Forbidden combo")
    else:
        None
#        print("No forbidden combos")
    
    return (True, None)

good_count = 0
bad_count = 0
input = sys.stdin.readline().rstrip()
while input:
    (result, reason) = str_test(input)
    if result:
        print("%s - Good" % input)
        good_count += 1
    else:
        print("%s - Bad - %s" % (input, reason))
        bad_count += 1
    input = sys.stdin.readline().rstrip()

print("Good: %d Bad: %d" % (good_count, bad_count))
