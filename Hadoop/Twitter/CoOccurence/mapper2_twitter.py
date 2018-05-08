#!/usr/bin/env python
"""mapper.py"""

import sys

from collections import defaultdict
from operator import itemgetter
from nltk.corpus import stopwords

a=sorted(open("TwitterWords/part-00000").readlines(), reverse=True, key=lambda line: int(line.split('\t')[1]))

cnt=0
topten=list()
for b in a:
	if(cnt<10):
		topten.append(b.split('\t')[0])
		cnt=cnt+1
	
com = defaultdict(lambda : defaultdict(int))
#stri="horse ink rabbit boy horse rabbit default dict int"

my_stopset=set(stopwords.words('english'))
my_stopset.add("rt")
my_stopset.add("https")
my_stopset.add("co")
my_stopset.add("said")
for line in sys.stdin:
	line=line.strip()
	terms_only=line.split()
	for i in range(len(terms_only)-1):
		for j in range(i+1, len(terms_only)):
			w1, w2 = sorted([terms_only[i], terms_only[j]])                
			if w1 != w2:
				if w1 in topten and w2 in topten:
					if w1.lower() not in my_stopset and w2.lower() not in my_stopset:
						com[w1][w2] += 1

com_max = []
# For each term, look for the most common co-occurrent terms
for t1 in com:
    t1_max_terms = sorted(com[t1].items(), key=itemgetter(1), reverse=True)
    for t2, t2_count in t1_max_terms:
        com_max.append(((t1, t2), t2_count))
# Get the most frequent co-occurrences
terms_max = sorted(com_max, key=itemgetter(1), reverse=True)
for j in range(len(terms_max)):
	strin=terms_max[j][0][0]+","+terms_max[j][0][1]
	print '%s\t%s' % (strin, terms_max[j][1])
#print '%s\t%s' % ("ink,int", "1")
