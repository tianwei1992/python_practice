#2-3.py
#to print a sentense in the midlle of a box
sentense=input("Sentence:")
screen_width=80
text_width=len(sentense)
box_width=text_width+6
left_margin=(screen_width-box_width)//2
print
print(' '*left_margin+'+'+'-'*(box_width-2)+'+')
print(' '*(left_margin+4)+'|'+' '*text_width+'|')
print(' '*(left_margin+4)+'|'+sentense+'|')
print(' '*(left_margin+4)+'|'+' '*text_width+'|')
print(' '*left_margin+'+'+'-'*(box_width-2)+'+')
print

