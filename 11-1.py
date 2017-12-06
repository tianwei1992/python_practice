#11-1.py
#pipeline
#somescript.py
#sys.stdin
#sys.stdout
#sys.stderror
import sys
sys.path.append('..')
import foo2
import sys
text=sys.stdin.read()
words=text.split()
count=len(words)
print('contain %d words'%count)

