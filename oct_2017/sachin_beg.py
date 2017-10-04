punc = ''':;!?.,_-(){}[]'"'''
str = input("enter the String")
new = ""
for char in range str:
   if char not in punc:
      new = new + char
print (new)
