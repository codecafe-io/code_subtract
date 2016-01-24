#!/usr/bin/env python
__author__="codecafe-io"

'''
Problem question: 
There are 2 input variables x,y
x represents how many inputs to be given on a single line with space
y represents the difference to check for

Problem output:
	example given below:
	5 2
	123 234 345 236 98

	answer: 1 (only one value has a difference of 2 {between 234 and 236})

Version:
python 3.4.1
'''

try:
    a,b=0,0
    print ("Please enter x as number of inputs and y as difference to check for")
    a,b=input().strip().split()
except: 
    print ("Please enter 2 chars")

hold=[]
hold=input().strip().split()
ct=0

if int(a) != len(hold): print ("Please enter only allowed number in the input"); exit();

for c in range(len(hold)):
	for d in range(len(hold)):
		if int(hold[c]) - int(hold[d]) == int(b):
			ct +=1;
	
print ("Number of matching pairs with the given difference is: ",ct)
