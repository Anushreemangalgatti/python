#Swapcase()with non-English character

sentance="i want say something to you"

#converts this sentance into uppercase
print(sentance.swapcase())

#perform swapcase() on sentance.swapcase()
print(sentance.swapcase().swapcase())

print(sentance.swapcase().swapcase().swapcase()==sentance)

#output
#I WANT SAY SOMETHING TO YOU
#i want to say something to you
#False