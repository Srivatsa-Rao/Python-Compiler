#!/usr/bin/python
import re

regexes=[
    re.compile('int'),
    re.compile('char')
]
i=0
fp1=open('text.txt','r')
fp2=open('temp2.txt','a')
for lines in fp1:
     linetemp=lines.splitlines()
     if any(regex.match(lines) for regex in regexes):
      fp2.write("Keyword")


      for singleline in lines:
          a[i]=singleline
          i+=1

     for singleline in lines:
       pass
