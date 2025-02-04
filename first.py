afsal=5.5
mani=6.6

#  or operator
#  in1   in2  op  0 - false  1 - true
#  0      0    0
#  0      1    1
#  1      0    1
#  1      1    1
print(afsal<mani) #a is lessthan b  true
print(mani<afsal) # b is a lessthan a  - false
print(afsal<mani or mani < afsal)
print(mani<afsal and mani>afsal)
print(not(mani<afsal and mani>afsal))