#! /usr/bin/python

def func(letter):
#here i created set of values without in a temp file called temp.txt
 tempfile=open('temp.txt','a');
 if(letter==';'):
  tempfile.write(';\n')
 #elif (letter.spilt()):
#     pass
 else:
  tempfile.write(letter)
