#!/usr/bin/python
fp1=open('temp.txt','r')
fp2=open('temp2.txt','a')
for lines in fp1:
 for single in lines:
     fp2.write(single)
     fp2.write("\n")
