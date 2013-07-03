#!/usr/bin/python

import sys
if len(sys.argv) != 2 :
    print "Please supply a filename"
    raise SystemExit(1)

fvalues = [float(line) for line in open(sys.argv[1])]

print "The minimum value is ", min(fvalues)
print "The maximum value is ", max(fvalues)
