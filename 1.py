#!/usr/bin/python
import lex
import sys
import fileinput
er="Syntax Error"

def main():
  i=0;
  print "Your file is "+sys.argv[1]
  lines = open(sys.argv[1]).read().splitlines()
  for singleline in lines:
      singlelinemodified=singleline.lstrip().rstrip()
      for letter in singlelinemodified:
        if(letter == '#'):
          print "comment skipped"
          break
        else:lex.func(letter)
      i+=1
      print "Parsed line",i


  import lex3









if __name__ == '__main__':
    main()
