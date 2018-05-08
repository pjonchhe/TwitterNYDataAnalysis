#!/usr/bin/env python
"""mapper.py"""

import sys
from nltk.corpus import stopwords

# input comes from STDIN (standard input)
#file=open("temp.txt","a+")
my_stopset=set(stopwords.words('english'))
my_stopset.add("rt")
my_stopset.add("https")
my_stopset.add("co")
my_stopset.add("said")
for line in sys.stdin:
    # remove leading and trailing whitespace
    #file.write(line)
    #file.write("utsav")
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
	if word.lower() not in my_stopset:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        	print '%s\t%s' % (word.lower(), 1)
#file.close()
